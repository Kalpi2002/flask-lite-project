<<<<<<< Updated upstream
from flask import render_template, request, redirect, url_for, flash
from flask import Flask
=======
# app.py
from flask import Flask, render_template, request, redirect, url_for, abort, flash
>>>>>>> Stashed changes
from models import db, Task
from forms import DeleteForm
from flask_wtf import CSRFProtect
import os

app = Flask(__name__)
# use a proper secret in production; for dev you can use a fixed string or env var
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
<<<<<<< Updated upstream
app.secret_key = "your_secret_key_here"  # Needed for flash messages
db.init_app(app)
=======
>>>>>>> Stashed changes

# init extensions
db.init_app(app)
csrf = CSRFProtect(app)

# create DB tables (runs on start if not created)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('list_tasks'))

@app.route('/tasks')
def list_tasks():
    tasks = Task.query.order_by(Task.id).all()
    delete_form = DeleteForm()
    return render_template('list.html', tasks=tasks, delete_form=delete_form)

# small add route for quick testing (optional)
@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if not title:
            flash('Title is required', 'error')
            return redirect(url_for('add_task'))
        t = Task(title=title, description=description)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('list_tasks'))
    return '''
      <h2>Add Task</h2>
      <form method="post">
        Title: <input name="title" required><br>
        Description: <textarea name="description"></textarea><br>
        <button type="submit">Add</button>
      </form>
      <p><a href="/tasks">Back to list</a></p>
    '''

# ===== DELETE route (POST) with CSRF & confirm on client side =====
@app.route('/task/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    form = DeleteForm()
    # validate_on_submit checks CSRF token automatically for POST
    if not form.validate_on_submit():
        abort(400, description="Invalid request (CSRF token missing or invalid).")
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{task.title}" deleted.', 'success')
    return redirect(url_for('list_tasks'))

@app.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Server-side validation
        if not title.strip():
            flash("Title is required!", "error")
            return redirect(url_for('create_task'))

        # Save new task
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()

        flash("Task created successfully!", "success")
        return redirect(url_for('list_tasks'))

    return render_template('form.html', action="Create", task=None)


if __name__ == '__main__':
    app.run(debug=True)

