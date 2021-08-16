from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student import Student
import repositories.student_repository as student_repository
import repositories.student_course_repository as student_course_repository

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

#Create -- TO DO
@students_blueprint.route("/students", methods = ["POST"])
def create_student():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    telephone = request.form["telephone"]
    level = request.form["level"]
    enrolled = request.form["enrolled"]
    new_student = Student(first_name, last_name, email, telephone, level, enrolled)
    student_repository.save(new_student)
    return redirect("/students")

#Edit
@students_blueprint.route("/students/<id>/edit")
def edit_student(id):
    student = student_repository.select(id)
    return render_template("students/edit.html", student = student)

#Update
@students_blueprint.route("/students/<id>", methods=["POST"])
def update_student(id):
    #insert code
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    telephone = request.form["telephone"]
    level = request.form["level"]
    enrolled = request.form["enrolled"]
    student = Student(first_name, last_name, email, telephone, level, enrolled, id)
    student_repository.update(student)
    return redirect("/students")

#Delete
@students_blueprint.route("/students/<id>/delete", methods=["POST"])
def delete_student(id):
    student_repository.delete(id)
    return redirect("/students")


#Show - not sure if works
@students_blueprint.route("/students/<id>")
def show_student(id):
    student = student_repository.select(id)
    # courses = student_course_repository.select(id)
    return render_template("students/show.html", student = student)
#courses=courses
#Add course to student (/students/<student_id>/add_course)
