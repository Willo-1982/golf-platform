from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

import models, schemas, auth, database

load_dotenv()  # load variables from .env file into os.environ

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

app = FastAPI()

# Setup CORS (so your Netlify, Streamlit can call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; lock to your domains later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "Golf Platform API is running!"}

# Example secured route
from fastapi import Depends
from auth import get_current_user

@app.get("/me")
def get_me(user=Depends(get_current_user)):
    return user

# Include your other routers / logic here
