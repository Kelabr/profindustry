from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from ...db.connection import connection
from ...db.schemas import CreateUser, DeleteUser
from ...db.querys import createUsers, deleteUser


router = APIRouter()
coon = connection()



@router.post('/create')
def create_user(newUser:CreateUser):
    response = createUsers(coon, newUser.name, newUser.email, newUser.phone, newUser.password, newUser.sex)

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': 'Created User'}
        )


@router.delete('/delete')
def delete_user(emailUser:DeleteUser): # Provavelmente vai ocorrer alteração -> 'email' não será pego pelo body mas sim pela token vindo pelo cookie
    response = deleteUser(coon, emailUser.email )

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': f'Usuário deletdo - email: {emailUser.email} '}
        )