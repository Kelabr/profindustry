from pydantic import BaseModel

class CreateUser(BaseModel):
    name:str
    email:str
    phone:str
    password:str
    sex:str

class DeleteUser(BaseModel):
    email:str

class LoginUser(BaseModel):
    email:str
    password:str

class ResponseUser(BaseModel):
    menssage:str