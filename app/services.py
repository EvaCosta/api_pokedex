import httpx
from cache import cache
from models import Pokemon, PaginatedPokemons, PokemonDetails
import xml.etree.ElementTree as ET
from fastapi import HTTPException, Response

# URL base da PokeAPI
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon"

class PokemonService:
    @staticmethod
    async def list_pokemons(offset: int, limit: int) -> PaginatedPokemons:
        cache_key = f"list_pokemons_{offset}_{limit}"
        
        if cache_key in cache:
            return cache[cache_key]
        
        async with httpx.AsyncClient() as client:
            try:
                params = {"offset": offset, "limit": limit}
                response = await client.get(POKEAPI_BASE_URL, params=params)
                response.raise_for_status()
    
                data = response.json()
                pokemons = data.get("results", [])
    
                # Ordena os pokémons pelo nome
                pokemons_sorted = sorted(pokemons, key=lambda p: p['name'])
    
                # Adiciona links para os detalhes de cada Pokémon
                for pokemon in pokemons_sorted:
                    pokemon_name = pokemon['name']
                    pokemon['detail_url'] = f"/pokemon/{pokemon_name}"
    
                # Monta a resposta paginada
                paginated_pokemons = PaginatedPokemons(
                    count=len(pokemons_sorted),
                    next=data.get("next"),
                    previous=data.get("previous"),
                    results=pokemons_sorted
                )
                cache[cache_key] = paginated_pokemons  # Armazena no cache
                return paginated_pokemons
            
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="Error fetching pokémons: " + str(e))
            
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail="Request error: " + str(e))

    @staticmethod
    async def pokemon_details(pokemon_name: str) -> PokemonDetails:
        async with httpx.AsyncClient() as client:
            try:
                # Fetch basic information about the Pokémon
                pokemon_url = f"{POKEAPI_BASE_URL}/{pokemon_name.lower()}"
                response = await client.get(pokemon_url)
                response.raise_for_status()
                pokemon_data = response.json()
    
                # Extract necessary details from the response
                abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
                types = [type['type']['name'] for type in pokemon_data['types']]
                height = pokemon_data['height']
                weight = pokemon_data['weight']
                image_url = pokemon_data['sprites']['front_default']
    
                # Create the detailed response model
                pokemon_details = PokemonDetails(
                    name=pokemon_data['name'],
                    abilities=abilities,
                    types=types,
                    height=height,
                    weight=weight,
                    image_url=image_url
                )
    
                return pokemon_details
    
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise HTTPException(status_code=404, detail=f"Pokémon '{pokemon_name}' not found")
                else:
                    raise HTTPException(status_code=e.response.status_code, detail="Error fetching Pokémon details")
    
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")

class ExportService:
    @staticmethod
    async def export_pokemons_to_xml() -> str:
        async with httpx.AsyncClient() as client:
            try:
                # Obter todos os pokémons da PokeAPI
                response = await client.get(POKEAPI_BASE_URL)
                response.raise_for_status()
    
                data = response.json()
                pokemons = data.get("results", [])
    
                # Ordena os pokémons pelo nome
                pokemons_sorted = sorted(pokemons, key=lambda p: p['name'])
    
                # Cria o elemento raiz <pokemons>
                root = ET.Element("pokemons")
    
                # Itera sobre cada pokemon e adiciona ao XML
                for pokemon in pokemons_sorted:
                    pokemon_element = ET.SubElement(root, "pokemon")
                    name_element = ET.SubElement(pokemon_element, "name")
                    name_element.text = pokemon['name']
                    url_element = ET.SubElement(pokemon_element, "url")
                    url_element.text = pokemon['url']
    
                # Converte o ElementTree em uma string XML
                xml_str = ET.tostring(root, encoding='utf-8', method='xml')
    
                # Retorna a string XML gerada
                return xml_str.decode('utf-8')
    
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="Error fetching pokémons: " + str(e))
    
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail="Request error: " + str(e))
