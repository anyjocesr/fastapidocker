from fastapi import FastAPI, HTTPException
from endpoints import router

app = FastAPI()
app.include_router(router)