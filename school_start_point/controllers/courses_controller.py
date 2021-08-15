from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

#Index
@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses = courses)

#New
@courses_blueprint.route("/courses/new")
def new_course():
    return render_template("courses/new.html")

#Create
@courses_blueprint.route("/courses", methods = ["POST"])
def create_course():
    pass

#Edit
@courses_blueprint.route("/courses/<id>/edit")
def edit_course(id):
    course = course_repository.select(id)
    return render_template("sessions/edit.html")

#Update

#Delete

#Show