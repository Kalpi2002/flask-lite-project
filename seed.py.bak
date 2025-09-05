from app import app, db
from models import Task

with app.app_context():
    # Create tables if they don't exist
    db.create_all()

    # Sample tasks
    task1 = Task(title="Buy groceries", description="Milk, Bread, Eggs")
    task2 = Task(title="Read book", description="Finish Chapter 5")
    task3 = Task(title="Exercise", description="30 minutes jogging")

    # Add tasks to the session
    db.session.add_all([task1, task2, task3])
    db.session.commit()

    print("Database seeded successfully!")
