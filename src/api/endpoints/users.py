from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from ...db.connection import connection
from ...db.schemas import CreateUser, DeleteUser
from ...db.querys import createUsers, deleteUser, updateUser
from ...auth.security import createAccessToken


router = APIRouter()
coon = connection()



@router.post('/create')
def create_user(newUser:CreateUser):# Gerar token para enviar via httpOnly para o front 
    response = createUsers(coon, newUser.name, newUser.email, newUser.phone, newUser.password, newUser.sex)

    if response:
        data = {'name': newUser.name, 'email': newUser.email}
        token = createAccessToken(data)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': 'Created User', 'token': token}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={'menssage': 'Erro ao tentar cadastrar- Email já existente'}
        )


@router.delete('/delete')
def delete_user(emailUser:DeleteUser): # Provavelmente vai ocorrer alteração -> 'email' não será pego pelo body mas sim pela token vindo pelo cookie
    response = deleteUser(coon, emailUser.email )

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': f'Usuário deletdo - email: {emailUser.email} '}
        )


@router.put('/update')
def update_user(dataUserUpdate:dict):
    response = updateUser(coon, dataUserUpdate)

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': f'Usuário Atualizado'}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={'menssage': 'Erro ao atualizar '}
        )
    
    