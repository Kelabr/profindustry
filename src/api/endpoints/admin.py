from fastapi import APIRouter
from ...db.connection import connection

router = APIRouter()
coon = connection()

@router.get('/')
def teste_amdin():
    return{'menssage': 'ok admin'}