#install and import flask_sqlalchemy

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# student/teach/review
# student has many reviews
# teacher has many reviews
# each review belongs to a student and a teacher

# student -> id, name, phase, email, superhere_partner, created_at, updated_at

# teacher -> id, name, favorite_language, email, favorite_food, created_at, updated_at

# review -> id, content, rating, student_id, teacher_id, created_at, updated_at

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    phase = db.Column(db.Integer)
    email = db.Column(db.String)
    superhero_parter = db.Column(db.String)

    reviews = db.relationship("Review", backref = "student")

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        print (f"<Student name={self.name} phase={self.phase}>")

class Teacher(db.Model):
    __tablename__="teachers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    favorite_language = db.Column(db.String)
    email = db.Column(db.String)
    favorite_food = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    reviews = db.relationship("Review", backref = "student")

    def __repr__(self):
        print (f"<Teacher name={self.name} favorite_language={self.favorite_language}>")
    
class Review(db.Model):
    __tablename__="reviews"

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    rating = db.Column(db.Float)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        print (f"<Teacher content={self.content} ratings={self.ratings} student_id={self.student_id} teacher_id={self.teacher_id}>")
    