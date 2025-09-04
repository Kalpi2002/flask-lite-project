from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev-secret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensure tables exist
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return redirect(url_for('list_tasks'))


@app.route('/tasks')
def list_tasks():
    q = request.args.get("q", "").strip()
    if q:
        tasks = Task.query.filter(Task.title.contains(q)).order_by(Task.created_at.desc()).all()
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("list.html", tasks=tasks, q=q)


@app.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        # Validation
        if not title or not description:
            flash('Both title and description are required.', 'danger')
            return render_template('form.html', task=None)

        # Save task
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully.', 'success')
        return redirect(url_for('list_tasks'))

    return render_template('form.html', task=None, action="Create")


@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        if not title or not description:
            flash('Both title and description are required.', 'danger')
            return render_template('form.html', task=task)

        task.title = title
        task.description = description
        db.session.commit()
        flash('Task updated successfully.', 'success')
        return redirect(url_for('list_tasks'))

    return render_template('form.html', task=task, action="Edit")


if __name__ == '__main__':
    app.run(debug=True)

