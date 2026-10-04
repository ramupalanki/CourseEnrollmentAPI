# Course Enrollment API

A simple REST API built using **Python and FastAPI** that allows students to enroll in courses.

The application demonstrates:

- FastAPI
- REST APIs
- HTTP methods
- Pydantic models
- Request validation
- HTTP exceptions
- CRUD-style operations
- Duplicate enrollment prevention
- Swagger UI API testing
- Git and GitHub workflow

---

## Project Structure

```text
course-enrollment-api/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI
- Git
- GitHub

---

## Installation

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Go to the project directory

```bash
cd course-enrollment-api
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI application using:

```bash
uvicorn main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

---

# Swagger UI

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to execute and demonstrate all APIs.

---

# APIs

## 1. Create Course

### Endpoint

```http
POST /courses
```

### Request

```json
{
  "id": 101,
  "name": "Python Programming",
  "description": "Learn Python programming from basics to advanced concepts"
}
```

### Response

```json
{
  "message": "Course created successfully",
  "course": {
    "id": 101,
    "name": "Python Programming",
    "description": "Learn Python programming from basics to advanced concepts"
  }
}
```

---

# 2. Get All Courses

### Endpoint

```http
GET /courses
```

### Response

```json
{
  "courses": [
    {
      "id": 101,
      "name": "Python Programming",
      "description": "Learn Python programming from basics to advanced concepts"
    }
  ]
}
```

---

# 3. Enroll Student

### Endpoint

```http
POST /enroll
```

### Request

```json
{
  "student_id": 1,
  "course_id": 101
}
```

### Response

```json
{
  "message": "Student enrolled successfully",
  "enrollment": {
    "enrollment_id": 1,
    "student_id": 1,
    "course_id": 101
  }
}
```

---

# 4. Get Student Courses

### Endpoint

```http
GET /students/{student_id}/courses
```

### Example

```http
GET /students/1/courses
```

### Response

```json
{
  "student_id": 1,
  "courses": [
    {
      "enrollment_id": 1,
      "course_id": 101,
      "course_name": "Python Programming",
      "description": "Learn Python programming from basics to advanced concepts"
    }
  ]
}
```

---

# 5. Delete Enrollment

### Endpoint

```http
DELETE /enroll/{enrollment_id}
```

### Example

```http
DELETE /enroll/1
```

### Response

```json
{
  "message": "Enrollment deleted successfully",
  "enrollment_id": 1
}
```

---

# Error Handling

The application returns meaningful HTTP errors.

## Course Not Found

If a student tries to enroll in a course that doesn't exist:

```json
{
  "detail": "Course not found"
}
```

HTTP status:

```text
404 Not Found
```

---

## Duplicate Enrollment

If a student tries to enroll in the same course twice:

```json
{
  "detail": "Student is already enrolled in this course"
}
```

HTTP status:

```text
400 Bad Request
```

---

## Enrollment Not Found

If an invalid enrollment ID is deleted:

```json
{
  "detail": "Enrollment not found"
}
```

HTTP status:

```text
404 Not Found
```

---

# Testing Flow

The recommended testing sequence is:

### Step 1

Create a course.

```http
POST /courses
```

### Step 2

Create another course.

```http
POST /courses
```

### Step 3

Get all courses.

```http
GET /courses
```

### Step 4

Enroll Student 1 in Course 101.

```http
POST /enroll
```

### Step 5

Try enrolling Student 1 in Course 101 again.

Expected result:

```text
400 Bad Request
```

### Step 6

Enroll Student 1 in another course.

```http
POST /enroll
```

### Step 7

Get all courses for Student 1.

```http
GET /students/1/courses
```

### Step 8

Delete an enrollment.

```http
DELETE /enroll/1
```

### Step 9

Try deleting the same enrollment again.

Expected result:

```text
404 Not Found
```

---

# API Summary

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/courses` | Create a course |
| GET | `/courses` | Get all courses |
| POST | `/enroll` | Enroll a student |
| GET | `/students/{student_id}/courses` | Get student's courses |
| DELETE | `/enroll/{enrollment_id}` | Delete enrollment |

---

# GitHub Submission

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Create Course Enrollment API"
```

Add your GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push the code:

```bash
git branch -M main
git push -u origin main
```

---

# YouTube Demonstration

Create a YouTube video demonstrating the complete application.

## Suggested Video Flow

### 1. Introduction

Explain:

> In this project, I have built a Course Enrollment API using Python and FastAPI. The application allows us to create courses, retrieve courses, enroll students, view student courses, and delete enrollments.

### 2. Explain Project Structure

Show:

```text
main.py
requirements.txt
README.md
```

### 3. Explain FastAPI Setup

Explain:

```python
app = FastAPI()
```

and the Pydantic models.

### 4. Demonstrate Create Course

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Execute:

```http
POST /courses
```

### 5. Demonstrate Get Courses

Execute:

```http
GET /courses
```

### 6. Demonstrate Enrollment

Execute:

```http
POST /enroll
```

with:

```json
{
  "student_id": 1,
  "course_id": 101
}
```

### 7. Demonstrate Duplicate Prevention

Execute the same enrollment again.

Show the:

```text
400 Bad Request
```

response.

Explain that the API checks whether the same student is already enrolled in the same course.

### 8. Demonstrate Student Courses

Execute:

```http
GET /students/1/courses
```

Explain how the API finds all enrollments for the student and returns the corresponding courses.

### 9. Demonstrate Delete Enrollment

Execute:

```http
DELETE /enroll/1
```

Show the successful response.

### 10. Demonstrate 404 Error

Try deleting the same enrollment again.

Show:

```text
404 Enrollment not found
```

### 11. Explain GitHub Repository

Show the GitHub repository containing:

```text
main.py
requirements.txt
README.md
```

---

# Submission

Submit the following:

### GitHub Repository

```text
YOUR_GITHUB_REPOSITORY_URL
```

### YouTube Video

```text
YOUR_YOUTUBE_VIDEO_URL
```

### Final Submission

```text
GitHub Repository:
YOUR_GITHUB_REPOSITORY_URL

YouTube Video:
YOUR_YOUTUBE_VIDEO_URL
```

---

## Learning Outcomes

After completing this project, you should understand:

- How to create a FastAPI application
- How REST APIs work
- GET, POST and DELETE methods
- Pydantic request models
- Path parameters
- HTTP status codes
- Exception handling
- API validation
- Duplicate data prevention
- Swagger UI
- API testing
- Git and GitHub
- How to document a Python project