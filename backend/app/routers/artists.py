from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ArtistOut)
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    return crud.create_artist(db, artist)

@router.get("/", response_model=list[schemas.ArtistOut])
def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_artists(db, skip, limit)

@router.get("/{artist_id}", response_model=schemas.ArtistOut)
def read_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@router.put("/{artist_id}", response_model=schemas.ArtistOut)
def update_artist(artist_id: int, artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = crud.update_artist(db, artist_id, artist)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@router.delete("/{artist_id}")
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    crud.delete_artist(db, artist_id)
    return {"detail": "Artist deleted"}

