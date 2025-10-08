from pydantic import BaseModel
from typing import List, Optional

# Album
class AlbumBase(BaseModel):
    title: str
    year: Optional[int] = None
    artist_id: int

class AlbumCreate(AlbumBase):
    pass

class AlbumOut(AlbumBase):
    id: int
    class Config:
        orm_mode = True

# Artist
class ArtistBase(BaseModel):
    name: str
    genre_id: int

class ArtistCreate(ArtistBase):
    pass

class ArtistOut(ArtistBase):
    id: int
    albums: List[AlbumOut] = []
    class Config:
        orm_mode = True

# Genre
class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreOut(GenreBase):
    id: int
    artists: List[ArtistOut] = []
    class Config:
        orm_mode = True

