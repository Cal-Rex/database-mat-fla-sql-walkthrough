# to run on an external hosting service:
# create requirements.txt file by using following console command:
#   pip freeze --local > requirements.txt
# create a Procfile for heroku with the follwoing steps:
#   use command in terminal:
#       touch Procfile
#   add the following command to the new file:
#       web: python run.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# if/else statement needed to be applied here to ensure project connected to elephantSQL  # noqa
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# To ensure that SQLAlchemy can also read our external database, #
# its URL needs to start with “postgresql://”, but we should not change this in the environment variable.  # noqa
# Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL  # noqa
# in case it starts with postgres://:
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)

from taskmanager import routes  # noqa
