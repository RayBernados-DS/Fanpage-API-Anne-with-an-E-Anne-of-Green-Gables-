from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.seed import seed_data
from app.database import SessionLocal, engine, Base
from app.models import Character, Actor
from app.schemas import CharacterResponse, ActorResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Anne With An E Fanbase API"
)

@app.on_event("startup")
def startup_event():
    seed_data()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Fanbase API is live."}


@app.get("/characters", response_model=list[CharacterResponse])
def get_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()


@app.get("/characters/{character_id}", response_model=CharacterResponse)
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(
        Character.id == character_id
    ).first()

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character not found"
        )

    return character


@app.get("/actors", response_model=list[ActorResponse])
def get_actors(db: Session = Depends(get_db)):
    return db.query(Actor).all()