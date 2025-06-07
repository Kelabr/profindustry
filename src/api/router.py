from fastapi import APIRouter
from .endpoints import users, admin
from ..db.connection import connection

api_router = APIRouter()


api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(admin.router, prefix='/admin', tags=['admin'])
