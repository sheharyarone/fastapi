# main.py
from fastapi import FastAPI
from app.routers.items import router as example_router
from app.db import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(example_router)
