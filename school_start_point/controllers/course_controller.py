from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
from repositories import course_repository, student_course_repository
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route('/courses')
def list_all_courses():
    courses = course_repository.select_all()
    return render_template('courses/index.html', courses = courses)