
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    
new_student= {"name": "Sunil"}
result= Student(**new_student)
# print(result)


#default / Optional Values
#With the help of Pydantic we can directly validate Emails like whether it is a valid email or not. if it finds that this is not a valid email then it will through an error.

class Family(BaseModel):
    name: Optional[str]= "Sunil"      # By default "name" will be "Sunil". If some value will be passed then it must be an str, otherwise it will through an error.
    age: Optional[int]= None          # But here Pydantic is smart enough that if we mistakly pass age value as string then it automatically, in beckand, converts this "str" value into "int".
    email: EmailStr                 # Here EmailStr is a built-in datatype in the Pydantic.
    cgpa: Optional[float] = Field(gt= 0, lt= 10, default= None, description= "A decimal value representing the cgpa of the student")  # Here "gt"--> greater than, "lt"--> less than.
    
new_member= {"age": "22", "email": "abc@gail.com", "cgpa": 7.88}
res= Family(**new_member)

res_dict= dict(res)
res_json= res.model_json_schema()
print(res_dict["name"])
print(res_json)
