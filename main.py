from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Course Enrollment API",
    description="A simple FastAPI application for managing courses and student enrollments",
    version="1.0.0"
)


# -----------------------------
# Data Models
# -----------------------------

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

courses = []

enrollments = []

next_enrollment_id = 1


# -----------------------------
# POST /courses
# Create a new course
# -----------------------------

@app.post("/courses", status_code=201)
def create_course(course: Course):

    # Check if course already exists
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
# Enroll student in course
# -----------------------------

@app.post("/enroll", status_code=201)
def enroll_student(request: EnrollmentRequest):

    global next_enrollment_id

    # Check whether student exists
    # For this small application, a student is considered
    # valid when the student_id is a positive number.
    if request.student_id <= 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Check whether course exists
    course = None

    for existing_course in courses:
        if existing_course.id == request.course_id:
            course = existing_course
            break

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

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
        "student_id": request.student_id,
        "course_id": request.course_id
    }

    enrollments.append(enrollment)

    next_enrollment_id += 1

    return {
        "message": "Student enrolled successfully",
        "enrollment": enrollment
    }


# -----------------------------
# GET /students/{student_id}/courses
# Get courses for a student
# -----------------------------

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):

    # Check whether student ID is valid
    if student_id <= 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_enrollments = []

    for enrollment in enrollments:
        if enrollment["student_id"] == student_id:
            student_enrollments.append(enrollment)

    # If student has no enrollment
    if not student_enrollments:
        return {
            "student_id": student_id,
            "courses": []
        }

    student_courses = []

    for enrollment in student_enrollments:

        for course in courses:

            if course.id == enrollment["course_id"]:

                student_courses.append({
                    "enrollment_id": enrollment["enrollment_id"],
                    "course_id": course.id,
                    "course_name": course.name,
                    "description": course.description
                })

    return {
        "student_id": student_id,
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