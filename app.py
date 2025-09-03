from flask import Flask, render_template, redirect, url_for
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

@app.route('/')
def home():
    return redirect(url_for('list_tasks'))

@app.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return render_template('list.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)

