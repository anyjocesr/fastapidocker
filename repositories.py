from typing import List, Optional
from uuid import UUID, uuid4
from schema import Usuario, NuevoUsuario, UserResponseSingin
#from fastapi import FastAPI, HTTPException
#from fastapi.responses import JSONResponse




class UsuarioRepository:
    def __init__(self):
        self._usuarios: List[Usuario] = []
    
    def lista_usuarios(self) -> List[Usuario]:
        return self._usuarios
        

    def singup(self, data: NuevoUsuario) -> List[Usuario]:
        nuevo = Usuario(id=uuid4(), **data.dict())
        self._usuarios.append(nuevo)
        return nuevo
    
    def obtener_usuario(self, usuario_id: UUID):
        # completar la parte de sing in, y crear una base de datos jiji
        return next((a for a in self._usuarios if a.id == usuario_id), None)
    
    def singin(self, usuario_id :UUID,data:Usuario) -> Optional[Usuario]:
        usuario = self.obtener_usuario(usuario_id)

        """
        if not usuario:
            raise HTTPException(status_code=404,detail="user not found")

        if usuario.email != data.email:
            print("El usuario no existe")
            raise HTTPException(status_code=404, detail="Bad email")
        
        if usuario.password != data.password:
            print("La contraseña es incorrecta")
            raise HTTPException(status_code=404, detail="Bad password")
    
        return JSONResponse(content=usuario.model_dump(), status_code=202)
        """
        
        success = True 
        message = "Signin success"
        if not usuario:
            success = False
            message="user not found"

        elif usuario.email != data.email:
            success = False
            message="Bad email"
            
        elif usuario.password != data.password:
            success = False
            message="Bad password"

        return UserResponseSingin(
            success = success,
            message = message
        )