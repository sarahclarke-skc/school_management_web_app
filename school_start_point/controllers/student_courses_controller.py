from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student_course import Student_Course
import repositories.course_repository as course_repository
import repositories.student_course_repository as student_course_repository
import repositories.student_repository as student_repository

student_courses_blueprint = Blueprint("student_courses", __name__)