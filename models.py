from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    due_date = db.Column(db.Date)

    priority = db.Column(db.Integer, default=2)

    status = db.Column(db.Integer, default=0)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    completed_at = db.Column(db.DateTime)

    def mark_complete(self):
        self.status = 1
        self.completed_at = datetime.utcnow()

    def mark_incomplete(self):
        self.status = 0
        self.completed_at = None
