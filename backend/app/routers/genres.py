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

@router.post("/", response_model=schemas.GenreOut)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)

@router.get("/", response_model=list[schemas.GenreOut])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_genres(db, skip, limit)

@router.get("/{genre_id}", response_model=schemas.GenreOut)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@router.put("/{genre_id}", response_model=schemas.GenreOut)
def update_genre(genre_id: int, genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = crud.update_genre(db, genre_id, genre)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@router.delete("/{genre_id}")
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    crud.delete_genre(db, genre_id)
    return {"detail": "Genre deleted"}

