from fastapi import FastAPI

app = FastAPI(
    title="FastAPI",
    description="Curso de FastAPI",
    version="0.1.0",
) 

#Endpoint de ejemplo
@app.get("/",tags=['Inicio']) #ruta principal
def read_root():
    return {"Hello": "World"}


