from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # when page is loaded, the variable below queries the Category table for all entries, and then orders them by name
    # wrapping the variable value in a list( ) tag orders the data in the form of a list/array
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories=categories explained:
    # categories #1 = is the variable name that refers to categories.html
    # categories #2 = is the variable defined inside this function (categories = list(...) )
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