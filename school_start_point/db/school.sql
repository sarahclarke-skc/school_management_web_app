DROP TABLE student_courses;
DROP TABLE students;
DROP TABLE courses;

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    telephone VARCHAR(255),
    level VARCHAR(255),
    enrolled BOOLEAN
);

CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    level VARCHAR(255),
    days VARCHAR(255),
    start_time VARCHAR(255),
    duration INT,
    length_of_course VARCHAR(255)
);

CREATE TABLE student_courses(
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    grade VARCHAR(255)
);