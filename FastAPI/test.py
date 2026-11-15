from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2  # type: ignore[reportMissingModuleSource]
from psycopg2.extras import RealDictCursor  # type: ignore[reportMissingModuleSource]

app = FastAPI()

db_url = "postgresql://neondb_owner:npg_vdG9tMgXPu1m@ep-dawn-fog-beeby6s8-pooler.c-9.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

class Student(BaseModel):
    id:int
    name: str
    age: int

def get_connection():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    # uv add psycopg2-binary
    return conn


def save_student_to_file(data: Student):
    with open("students.txt", "a") as f:
        f.write(f"{data.id}, {data.name}, {data.age}\n")

@app.post("/students")
def create_student(stud: Student):
    save_student_to_file(stud)
    return {"msg": "Student data saved successfully"}

@app.post("/students/db/insert")
def store_students_in_db(student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(
        insert_query, (student.id, student.name, student.age)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "Student data inserted into the database successfully"}

# /update and /delete endpoints for the student data in the database