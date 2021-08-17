from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student_course import Student_Course
import repositories.student_course_repository as student_course_repository
import repositories.course_repository as course_repository
import repositories.student_repository as student_repository

student_courses_blueprint = Blueprint("student_courses", __name__)

#Index --> should I use the route as student_course OR should I use 'enrolment'?
@student_courses_blueprint.route("/student_courses")
def student_course():
    student_courses = student_course_repository.select_all()
    return render_template("student_courses/index.html", student_courses = student_courses )

#New
@student_courses_blueprint.route("/student_courses/new")
def new_student_course():
    return render_template("student_courses/new.html")

#Create TO DO
@student_courses_blueprint.route("/student_courses", methods=['POST'])
def create_student_course():
    pass

#Edit
@student_courses_blueprint.route("/student_courses/<id>/edit")
def edit_student_course(id):
    student_course = student_course_repository.select(id)
    return render_template("student_courses/edit.html", student_course = student_course)

#Update

#Delete
@student_courses_blueprint.route("/student_courses/<id>/delete", methods=['POST'])
def delete_student_course(id):
    student_course_repository.delete(id)
    return redirect("/student_courses")

#Show

#Add student to course?