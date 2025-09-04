from flask import Flask
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return '<br>'.join([f"{t.id} - {t.title}" for t in tasks])

if __name__ == '__main__':
    app.run(debug=True)
