from flask import Flask, render_template
from controllers.student_courses_controller import student_courses_blueprint
from controllers.courses_controller import courses_blueprint
from controllers.students_controller import students_blueprint

app = Flask(__name__)

app.register_blueprint(student_courses_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(students_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)