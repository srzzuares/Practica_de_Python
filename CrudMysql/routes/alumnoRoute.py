from fastapi import APIRouter

router = APIRouter()
alumnos=[]

@router.get("/getAllAlumnos")
def getAll():
    return alumnos