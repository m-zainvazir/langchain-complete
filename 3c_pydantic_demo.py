from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str ="Zain"
    age: Optional[int] = None #Even if you provide number in string, Pydantic will convert it to int
    email: EmailStr #Validates email format
    cgpa : float = Field(gt=0, le=10, default=5, description="A decimal value representing the CGPA")

new_student = {"age": 20, "email": "mndnd@gmail.com", "cgpa": 1}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])
student_json = student.model_dump_json()