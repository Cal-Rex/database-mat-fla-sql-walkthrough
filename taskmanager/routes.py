from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    # call on the Task variable in model and
    # query its table for all entries
    # make sure to wrap it in a list so that it
    # can be understood and used by other python functions!
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


# +------ Categories, routes and functions ----------+
@app.route("/categories")
def categories():
    # when page is loaded, the variable below queries the Category table for
    # all entries, and then orders them by name
    # wrapping the variable value in a list( ) tag orders
    # the data in the form of a list/array
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories=categories explained:
    # categories #1 = is the variable name that refers to categories.html
    # categories #2 = is the variable defined inside this function
    #                 (categories = list(...) )
    return render_template("categories.html", categories=categories)


# the first method applied here is regarded as the default method
# (that would be GET, in this instance)
# however, if the page is loaded with a POST action...
# (like when a form is submitted and results in it loading)
# the if statement will run instead
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # creates new instance of the "Category" model
        # imported at the top of the file
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# in the @app.route, when determining the route as the first argument,
# the variable created in the second parameter in the edit_category.html
# hrefs are added onto the /route
# because this variable is established outside of a python file
# (and in an html) the variable needs to be wrapped in < >.
# because the category id for the table is an integer, it is prefixed with int:
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
# after it is clarified in the route parameter,
# it needs to be added to the function,
# but the <int: > is no longer required
def edit_category(category_id):
    # the variable below queries the database with the value of
    # category_id provided from the html route and assigns that
    # value to a variable "category" inside the function
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        # as the following table item already exists,
        # we can just update the variable, instead of
        # having to add a new item to the table like in
        # the add_category route
        category.category_name = request.form.get("category_name")
        # as this is being done in the background/command line
        # the terminal needs to be instructed to commit
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


# +------ tasks, routes and functions ----------+
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # variable retrieves the values entered into the add task form
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("task_date"),
            Category_id=request.form.get("category_id")
            )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("task_date")
        task.Category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))