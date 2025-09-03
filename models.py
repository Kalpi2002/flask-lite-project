from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)          # Task ID
    title = db.Column(db.String(100), nullable=False)     # Task title (required)
    description = db.Column(db.Text, nullable=False)     # Task description (required)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp

    def __repr__(self):
        return f"<Task {self.title}>"
