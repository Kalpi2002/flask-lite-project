from flask import Flask, render_template, redirect, url_for, request
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev-secret'  # Needed for flash messages later

# Initialize DB
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()
    # Add sample tasks if DB is empty
    if Task.query.count() == 0:
        sample_tasks = [
            Task(title="Buy groceries", description="Milk, Bread, Eggs"),
            Task(title="Read book", description="Finish Chapter 5"),
            Task(title="Exercise", description="30 minutes jogging")
        ]
        db.session.add_all(sample_tasks)
        db.session.commit()

# Home redirects to task list
@app.route('/')
def home():
    return redirect(url_for('list_tasks'))

# List all tasks
@app.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return render_template('list.html', tasks=tasks)

# Delete a task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('list_tasks'))

if __name__ == '__main__':
    app.run(debug=True)

