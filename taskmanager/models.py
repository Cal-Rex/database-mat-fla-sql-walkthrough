# connect to the session database established in env.py (taskmanager)
from taskmanager import db


# "class"es are used to create tables
class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # nullable=False means it's a mandatory field
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    # all of the above info is then converted into a string ahead of output
    # by using __repr__ so that it prints properly
    def __repr__(self):
        # __repr__ stands for represent, which means:
        # "to represent itself in the form of a string"
        return self.category_name


class Task(db.Model):
    # schema for Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    Category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    # CASCADE, means to repeat the same command on child/related elements, like magic!
    # +-------------------------------------------------------------------------------+
    # full list of Column types can be found in the SQLAlchemy docs

    def __repr(self):
        # __repr__ stands for represent, which means:
        # "to represent itself in the form of a string"
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )