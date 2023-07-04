from fastapi import FastAPI
from routes.alumnoRoute import router
app = FastAPI()

app.include_router(router)