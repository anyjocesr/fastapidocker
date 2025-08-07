from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional

class UsuarioBase(BaseModel):
    email: str
    password: str

class NuevoUsuario(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id:UUID

class UserResponseSingin(BaseModel):
    success: bool
    message: str