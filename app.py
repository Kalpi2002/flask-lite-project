# app.py (only the new/changed parts)

from flask import Flask, render_template, redirect, url_for, request, flash   # make sure flash is imported
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev-secret'  # required for flash messages

db.init_app(app)

# ... keep your existing routes ...

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{task.title}" deleted.')
    return redirect(url_for('list_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
