from fastapi import FastAPI, HTTPException, Query, Response
from starlette.middleware.cors import CORSMiddleware
from services import PokemonService, ExportService
from models import PaginatedPokemons, PokemonDetails
import xml.etree.ElementTree as ET

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para listar os pokémons com paginação
@app.get("/pokemons/", response_model=PaginatedPokemons)
async def list_pokemons(offset: int = Query(0), limit: int = Query(20)):
    return await PokemonService.list_pokemons(offset, limit)

# Rota para detalhes de um pokémon
@app.get("/pokemon/{pokemon_name}", response_model=PokemonDetails)
async def pokemon_details(pokemon_name: str):
    return await PokemonService.pokemon_details(pokemon_name)

# Rota para exportar pokémons para XML
@app.get("/export/pokemons/xml/", response_class=Response, tags=["export"])
async def export_pokemons_to_xml():
    try:
        xml_str = await ExportService.export_pokemons_to_xml()
        return Response(content=xml_str, media_type="application/xml")
    except HTTPException as e:
        raise e
