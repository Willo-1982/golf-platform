# /fastapi-backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, auth, database
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth.create_user(db, user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return auth.authenticate_user(db, user.email, user.password)

@app.get("/me")
def get_me(current_user: models.User = Depends(auth.get_current_user)):
    return {"email": current_user.email, "name": current_user.name}

@app.get("/my-rounds")
def get_my_rounds(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    rounds = db.query(models.Round).filter(models.Round.user_id == current_user.id).all()
    return rounds

@app.get("/strokes-gained")
def get_strokes_gained(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    rounds = db.query(models.Round).filter(models.Round.user_id == current_user.id).all()
    # Fake example: you'd calculate vs benchmarks
    sg_tee = sum(r.sg_tee for r in rounds) / len(rounds) if rounds else 0
    sg_approach = sum(r.sg_approach for r in rounds) / len(rounds) if rounds else 0
    sg_putting = sum(r.sg_putting for r in rounds) / len(rounds) if rounds else 0
    return {
        "tee": round(sg_tee,2),
        "approach": round(sg_approach,2),
        "putting": round(sg_putting,2)
    }
