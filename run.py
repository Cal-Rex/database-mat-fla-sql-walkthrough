# to run on an external hosting service:
# create requirements.txt file by using following console command:
#   pip freeze --local > requirements.txt
# create a Procfile for heroku with the follwoing steps:
#   use command in terminal:
#       touch Procfile
#   add the following command to the new file:
#       web: python run.py
import os
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
