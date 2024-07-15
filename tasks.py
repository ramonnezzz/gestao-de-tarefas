from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'
