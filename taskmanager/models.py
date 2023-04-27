from taskmanager import db
# SQL Alchemy contains all column types under the db package


class Category(db.Model):
    # schema for category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task",
        Backref="category",
        cascade="all, delete",
        lazy=True
        )

    def __repr__(self):
        # __repr__ stands for represent, which means:
        # "to represent itself in the form of a string"
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )


class Task(db.Model):
    # schema for category model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey(
            category.id,
            ondelete="CASCADE"
            ),
        nullable=False)
