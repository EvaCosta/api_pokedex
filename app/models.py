from pydantic import BaseModel
from typing import Optional, List

class Pokemon(BaseModel):
    name: str
    url: str

class PaginatedPokemons(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Pokemon]

class PokemonDetails(BaseModel):
    name: str
    abilities: List[str]
    types: List[str]
    height: int
    weight: int
    image_url: str
