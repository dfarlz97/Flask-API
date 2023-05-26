# step 1: install Flask Library 
    # pipenv install 
    # pipenv shell
    # touch server
    # cd server
    # touch app.py
    # pipenv install Flask (from main directory)

#Step 2: import flask 
from flask import Flask

from flask_migrate import Migrate

from models import db, Student, Teacher, Review

#Step 3: create flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# migration --> init db 

Migrate(app, db)

db.init_app(app)

@app.route("/")
def index():
    return {"message": "Hello World!"}