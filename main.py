from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Course Enrollment API",
    description="API for managing courses and student enrollments",
    version="1.0.0"
)


# -----------------------------
# Data Models
# -----------------------------

class Student(BaseModel):
    id: int
    name: str


class Course(BaseModel):
    id: int
    name: str
    description: str


class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int


# -----------------------------
# In-Memory Data
# -----------------------------

students = [
    Student(id=1, name="Ravi"),
    Student(id=2, name="Anita"),
    Student(id=3, name="Rahul")
]

courses = []

enrollments = []

next_enrollment_id = 1


# -----------------------------
# Helper Functions
# -----------------------------

def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def get_course(course_id: int):
    for course in courses:
        if course.id == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# -----------------------------
# POST /courses
# Create a new course
# -----------------------------

@app.post("/courses", status_code=201)
def create_course(course: Course):

    for existing_course in courses:
        if existing_course.id == course.id:
            raise HTTPException(
                status_code=400,
                detail="Course with this ID already exists"
            )

    courses.append(course)

    return {
        "message": "Course created successfully",
        "course": course
    }


# -----------------------------
# GET /courses
# Get all courses
# -----------------------------

@app.get("/courses")
def get_courses():

    return {
        "courses": courses
    }


# -----------------------------
# POST /enroll
# Enroll a student in a course
# -----------------------------

@app.post("/enroll", status_code=201)
def enroll_student(request: EnrollmentRequest):

    global next_enrollment_id

    # Check whether student exists
    student = get_student(request.student_id)

    # Check whether course exists
    course = get_course(request.course_id)

    # Prevent duplicate enrollment
    for enrollment in enrollments:
        if (
            enrollment["student_id"] == request.student_id
            and enrollment["course_id"] == request.course_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Student is already enrolled in this course"
            )

    # Create enrollment
    enrollment = {
        "enrollment_id": next_enrollment_id,
        "student_id": student.id,
        "course_id": course.id
    }

    enrollments.append(enrollment)

    next_enrollment_id += 1

    return {
        "message": "Student enrolled successfully",
        "enrollment": enrollment
    }


# -----------------------------
# GET /students/{student_id}/courses
# Get all courses for a student
# -----------------------------

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):

    # Check whether student exists
    student = get_student(student_id)

    student_courses = []

    for enrollment in enrollments:

        if enrollment["student_id"] == student_id:

            course = get_course(enrollment["course_id"])

            student_courses.append({
                "enrollment_id": enrollment["enrollment_id"],
                "course_id": course.id,
                "course_name": course.name,
                "description": course.description
            })

    return {
        "student_id": student.id,
        "student_name": student.name,
        "courses": student_courses
    }


# -----------------------------
# DELETE /enroll/{enrollment_id}
# Delete an enrollment
# -----------------------------

@app.delete("/enroll/{enrollment_id}")
def delete_enrollment(enrollment_id: int):

    for enrollment in enrollments:

        if enrollment["enrollment_id"] == enrollment_id:

            enrollments.remove(enrollment)

            return {
                "message": "Enrollment deleted successfully",
                "enrollment_id": enrollment_id
            }

    raise HTTPException(
        status_code=404,
        detail="Enrollment not found"
    )
