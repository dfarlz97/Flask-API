# step 1: install Flask Library 
    # pipenv install 
    # pipenv shell
    # touch server
    # cd server
    # touch app.py
    # pipenv install Flask (from main directory)

#Step 2: import flask 
from flask import Flask

#Step 3: create flask application
app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Hello World!"}