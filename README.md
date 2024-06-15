# Pokémon API com FastAPI e Docker Compose

Este é um exemplo simples de uma API utilizando FastAPI e Docker Compose para listar e obter detalhes de Pokémon, integrando-se à PokeAPI para os dados.

## Pré-requisitos

Certifique-se de ter Docker e Docker Compose instalados em sua máquina. Você pode baixá-los em [docker.com](https://www.docker.com/get-started).

## Configuração e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/pokemon-api.git
   cd pokemon-api
   ```

2. Construa e inicie os serviços utilizando Docker Compose:

   ```bash
   docker-compose up --build
   ```

   Isso irá construir a imagem do Docker a partir do Dockerfile no diretório `./app` e iniciar o serviço FastAPI.

3. Após iniciar, acesse a documentação interativa da API em `http://127.0.0.1:8000/docs`. Lá você encontrará informações detalhadas sobre os endpoints disponíveis, parâmetros aceitos e exemplos de uso.

## Endpoints Disponíveis

### Listagem de Pokémons com Paginação

- Endpoint: `http://127.0.0.1:8000/pokemons/`
- Método: `GET`
- Parâmetros de consulta:
  - `offset` (int, opcional): Deslocamento para paginar os resultados (padrão: 0).
  - `limit` (int, opcional): Número máximo de resultados por página (padrão: 20).

### Detalhes de um Pokémon

- Endpoint: `http://127.0.0.1:8000/pokemon/{pokemon_name}`
- Método: `GET`
- Parâmetros:
  - `pokemon_name` (str): Nome do Pokémon desejado.