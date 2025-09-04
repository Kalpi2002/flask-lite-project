from flask import render_template, request, redirect, url_for, flash
from flask import Flask
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your_secret_key_here"  # Needed for flash messages
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
cat > app.py <<'PY'
from flask import Flask, render_template, request
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    q = request.args.get('q')
    if q:
        tasks = Task.query.filter(Task.title.contains(q)).all()
    else:
        tasks = Task.query.all()
    return render_template('list.html', tasks=tasks, query=q)

if __name__ == '__main__':
    app.run(debug=True)
PY
