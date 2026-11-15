from fastapi import FastAPI

app = FastAPI()

@app.get("/") # we hv provided the path to the function
# now this line of code is independent of the function and it will be 
# executed when the function is called.
def test() :
    return {"message": "Hello, World!"}
    
@app.get("/apicall") # we hv provided the path to the function

# uvicorn main:app --reload
def test1():
    return "This is a test function that is linrked to the path /apicall a new callwith reload"


@app.get("/apicall/learn/new/path") # we hv provided the path to the function
def test2():
    return "This is a test function that is linrked to the path /apicall a new callwith reload"

students = {1: "Akash", 2: "AMIT", 3: "Rohit", 4: "Ramesh", 5: "Suresh"}


@app.get("/students") # we hv provided the path to the function
def get_student():
    return students

@app.get("/students/{student_id}") # we hv provided the path to the function
def get_student_id(student_id: int):
    return {"id": student_id, "name": students[student_id]}


@app.post("/add_stu") # we hv provided the path to the function
def add_data():
    students["stud_id"] = "name"
    return students

# new method is http://127.0.0.1:8000/add_stu?stud_id=5&name=%22Sudhansu%22

from pydantic import BaseModel

class newdata(BaseModel):
    stud_id: int
    name: str


@app.post("/add_stu_new") # we hv provided the path to the function
def add_stud_new_value(new_data: newdata):
    students[new_data.stud_id] = new_data.name
    return students


