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
@courses_blueprint.route("/courses", methods=["POST"])
def create_course():
    name = request.form["name"]
    level = request.form["level"]
    days = request.form["days"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    length_of_course =request.form["length_of_course"]
    new_course = Course(name, level, days, start_time, duration, length_of_course)
    course_repository.save(new_course)
    return redirect("/courses")

#Edit
@courses_blueprint.route("/courses/<id>/edit")
def edit_course(id):
    course = course_repository.select(id)
    return render_template("courses/edit.html", course = course)

#Update
@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_course(id):
    #insert code
    name = request.form["name"]
    level = request.form["level"]
    days = request.form["days"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    length_of_course = request.form["length_of_course"]
    course = Course(name, level, days, start_time, duration, length_of_course, id)
    course_repository.update(course)
    return redirect("/courses")

#Delete
@courses_blueprint.route("/courses/<id>/delete", methods=["POST"])
def delete_course(id):
    course_repository.delete(id)
    return redirect("/courses")


#Show
@courses_blueprint.route("/courses/<id>/show")
def show_students(id):
    students = course_repository.get_students_on_course(id)
    return render_template("courses/show.html", students = students)