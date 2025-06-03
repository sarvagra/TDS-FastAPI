# %% intro
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()  # create an instance of FastAPI

'''
methods :
> GET    : get info 
> POST   : create new resource
> PUT    : update existing resource
> DELETE : delete existing resource
'''

# %% 
@app.get("/")  # decorator to define a route
def index():
    return {"name": "Sarvagra "}  # returns json response

# %% path parameters
# endpoint parameter

students = {
    1: {"name": "John", "age": 20, "year": "year 12"},
    2: {"name": "Jane", "age": 22, "year": "year 13"},
    3: {"name": "Doe", "age": 21, "year": "year 14"},
}

@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(..., description="The ID of the student to retrieve", gt=0, lt=4)
):  # adds conditions to take values only >0 and <4
    '''
    gt : greater than
    lt : less than
    ge : greater than or equal
    le : less than or equal
    et : equal to
    '''
    return students[student_id]  # get student by id

# %% query parameters
"""
@app.get("/get-by-name")
def get_by_name(name: str):  # to remove *required field, use default value as None {name: str = None}
    '''
    Query parameters are optional and can be used to filter results.
    '''
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {'message': 'Student not found'}
"""

# %% combining path and query parameters
@app.get("/get-by-name/{student_id}")
def get_by_name(student_id: int, name: str = None):
    '''
    Combines path and optional query parameter.
    '''
    student = students.get(student_id)

    if student is None:
        return {"message": "Student ID not found"}

    if name is None or student["name"].lower() == name.lower():
        return student

    return {"message": "Name does not match the student ID"}

# %% request body and POST 
class Student(BaseModel):
    name: str
    age: int
    year: str

@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    '''
    Creates a new student with the given ID.
    '''
    if student_id in students:
        return {"message": "Student ID already exists"}
    
    students[student_id] = student.model_dump()
    return students[student_id]

# %% update existing resource with PUT
class updatestudent(BaseModel):
    name: str = None
    age: int = None
    year: str = None

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updatestudent):
    '''
    Updates an existing student with the given ID.
    '''
    if student_id not in students:
        return {"message": "Student ID not found"}
    
    students[student_id] = student.model_dump()
    return students[student_id]

# update existing resource while keeping other details intact
@app.patch("/update-student-partially/{student_id}")
def update_student_partially(student_id: int, student: updatestudent):
    '''
    Partially updates an existing student with the given ID.
    '''
    if student_id not in students:
        return {"message": "Student ID not found"}
    
    existing_student = students[student_id]

    # Update only the fields that are provided
    for key, value in student.model_dump().items():
        if value is not None:
            existing_student[key] = value

    students[student_id] = existing_student
    return students[student_id]

# %% delete existing resource with DELETE
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    '''
    Deletes a student with the given ID.
    '''
    if student_id not in students:
        return {"message": "Student ID not found"}
    
    del students[student_id]
    return {"message": "Student deleted successfully"}
