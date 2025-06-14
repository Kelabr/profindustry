from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from fastapi import status
from ...db.connection import connection
from ...db.schemas import CreateUser, DeleteUser, LoginUser, ResponseUser
from ...db.querys import createUsers, deleteUser, updateUser, loginUser
# from ...auth.security import createAccessToken
from src.auth import createAccessToken


router = APIRouter()
coon = connection()



@router.post('/create', response_model=ResponseUser)
def create_user(newUser:CreateUser):# Gerar token para enviar via httpOnly para o front 
    response = createUsers(coon, newUser.name, newUser.email, newUser.phone, newUser.password, newUser.sex)

    if response:
        data = {'name': newUser.name, 'email': newUser.email}
        token = createAccessToken(data)


        res = JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': 'Created User', 'token': token}
        )

        res.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            # secure=True,
            samesite='lax',
            max_age=3600,
            path='/'
        )

        return res
    

    else:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={'menssage': 'Erro ao tentar cadastrar- Email já existente'}
        )


@router.delete('/delete', response_model=ResponseUser)
def delete_user(emailUser:DeleteUser): # Provavelmente vai ocorrer alteração -> 'email' não será pego pelo body mas sim pela token vindo pelo cookie
    response = deleteUser(coon, emailUser.email )

    if response:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': f'Usuário deletdo - email: {emailUser.email} '}
        )


@router.put('/update', response_model=ResponseUser)
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
    

@router.post('/login', response_model=ResponseUser)
def login_user(dataUserLogin:LoginUser):
    response = loginUser(coon, dataUserLogin.email, dataUserLogin.password)

    if response:

        token = createAccessToken(response)

        res = JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'menssage': 'Usuário logado', 'token': token}
        )
        
        res.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            # secure=True,
            samesite='lax',
            max_age=3600,
            path='/'
        )

        return res
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={'menssage':'Erro ao fazer login'}
        )
    

@router.post('/logout')
def logout_user(response:Response):
    response.delete_cookie(key="access_token", httponly=True)
    return{'menssage': 'Usuário deslogado'}



    