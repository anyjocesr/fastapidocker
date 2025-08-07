from fastapi import APIRouter
from typing import List
from uuid import UUID
from fastapi.responses import JSONResponse
from repositories import UsuarioRepository
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/sigin/{user_id}")
def singin(user_id:str):
    user_service = UsuarioRepository()
    response = user_service.singin(usuario_id=user_id,data={})

    if response.success:
        JSONResponse(status_code=200,content=response.message) 

    raise HTTPException(status_code=404, detail=response.message)


