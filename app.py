from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task   # assumes a models.py with SQLAlchemy Task model
from pathlib import Path

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(Path("tasks.db").resolve())
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dev-secret"

db.init_app(app)
with app.app_context():
    db.create_all()

# ----- LIST + SEARCH -----
@app.route("/", methods=["GET"])
def task_list():
    q = request.args.get("q", "").strip()
    if q:
        tasks = Task.query.filter(Task.title.contains(q)).order_by(Task.id.desc()).all()
    else:
        tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("list.html", tasks=tasks, q=q)

# ----- ADD -----
@app.route("/task/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if not title:
        flash("Title is required", "error")
        return redirect(url_for("task_list"))
    t = Task(title=title, description=description)
    db.session.add(t)
    db.session.commit()
    flash("Task added", "success")
    return redirect(url_for("task_list"))

# ----- DELETE -----
# 1) Confirm page (GET)
@app.route("/task/<int:task_id>/delete", methods=["GET"])
def delete_confirm(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("delete_confirm.html", task=task)

# 2) Delete action (POST)
@app.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for("task_list"))

# ----------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
