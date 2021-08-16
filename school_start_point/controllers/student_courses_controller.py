from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student_course import Student_Course
import repositories.course_repository as course_repository
import repositories.student_course_repository as student_course_repository
import repositories.student_repository as student_repository

student_courses_blueprint = Blueprint("student_courses", __name__)

#Index --> should I use the route as student_course OR should I use 'enrolment'?
@student_courses_blueprint.route("/student_course")
def student_course():
    student_courses = student_course_repository.select_all()
    return render_template("student_courses/index.html")

#New

#Create

#Edit

#Update

#Delete

#Show

#Add student to course?