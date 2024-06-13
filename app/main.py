from fastapi import FastAPI
from app.api import endpoints
from app.db.session import engine
from app.db.base import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Configuration Management API"}
