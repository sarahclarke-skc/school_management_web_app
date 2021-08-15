from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student import Student
import repositories.student_repository as student_repository

students_blueprint = Blueprint("students", __name__)

#Index
@students_blueprint.route("/students")
def students():
    students = student_repository.select_all()
    return render_template("students/index.html", students = students)

#New
@students_blueprint.route("/students/new")
def new_student():
    return render_template("students/new.html")