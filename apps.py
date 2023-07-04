from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Alumno(BaseModel):
    matricula:str
    nombre:str
    apellidos:str
    promedio:float
    cuatrimestre:int
    
@app.get("/getbyId/{matricula}")
def getStudent(matricula):
    print(matricula)
    response ={
        "message": "Peticion get "
    }

@app.get("/")
def saludar():
    response={
        "status":"Peticion por get recibida..."
    }
    return response

@app.post("/")
def insertAny(alumno:Alumno):
    print(alumno)
    response={
        "status":"Peticion por post recibida"
    }
    return response

@app.put("/")
def actualizarAny():
    response={
        "status":"Peticion por put recibida"
    }
    return response

@app.delete("/")
def borrarAny():
    response={
        "status":"Peticion por delete recibida"
    }
    return response