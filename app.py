from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task
from pathlib import Path

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(Path("tasks.db").resolve())
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dev-secret"

db.init_app(app)
with app.app_context():
    db.create_all()

# ------------------ ROUTES ------------------

# Home page → redirect to task list
@app.route("/")
def home():
    return redirect(url_for("list_tasks"))

# Task list with optional search
@app.route("/tasks")
def list_tasks():
    query = request.args.get("q", "").strip()
    if query:
        tasks = Task.query.filter(
            Task.title.contains(query) | Task.description.contains(query)
        ).order_by(Task.id.desc()).all()
    else:
        tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("list.html", tasks=tasks, q=query)

# Add new task
@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        if not title:
            flash("Title is required", "error")
            return redirect(url_for("add_task"))
        t = Task(title=title, description=description)
        db.session.add(t)
        db.session.commit()
        flash("Task added.", "success")
        return redirect(url_for("list_tasks"))
    return render_template("form.html", action="Add", task=None)

# Edit existing task
@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        if not title:
            flash("Title is required", "error")
            return redirect(url_for("edit_task", task_id=task_id))
        task.title = title
        task.description = description
        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for("list_tasks"))
    return render_template("form.html", action="Edit", task=task)

# Delete confirmation page
@app.route("/task/<int:task_id>/delete", methods=["GET"])
def delete_confirm(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("delete_confirm.html", task=task)

# Perform delete
@app.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for("list_tasks"))

# --------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
