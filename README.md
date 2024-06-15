# Pokémon API com FastAPI e Docker Compose

Este é um exemplo simples de uma API utilizando FastAPI e Docker Compose para listar e obter detalhes de Pokémon, integrando-se à PokeAPI para os dados.

## Pré-requisitos

Certifique-se de ter Docker e Docker Compose instalados em sua máquina. Você pode baixá-los em [docker.com](https://www.docker.com/get-started).

## Configuração e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/pokemon-api.git
   cd pokemon-api
   ```

2. **Construa e inicie os serviços utilizando Docker Compose:**

   ```bash
   docker-compose up --build
   ```

   Isso irá construir a imagem do Docker a partir do Dockerfile no diretório `./app` e iniciar o serviço FastAPI.

3. **Acesse a documentação interativa da API:**

   Após iniciar, acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Lá você encontrará informações detalhadas sobre os endpoints disponíveis, parâmetros aceitos e exemplos de uso.

## Endpoints Disponíveis

### Listagem de Pokémons com Paginação

- **Endpoint:** `http://127.0.0.1:8000/pokemons/`
- **Método:** `GET`
- **Parâmetros de consulta:**
  - `offset` (int, opcional): Deslocamento para paginar os resultados (padrão: 0).
  - `limit` (int, opcional): Número máximo de resultados por página (padrão: 20).

### Detalhes de um Pokémon

- **Endpoint:** `http://127.0.0.1:8000/pokemon/{pokemon_name}`
- **Método:** `GET`
- **Parâmetros:**
  - `pokemon_name` (str): Nome do Pokémon desejado.

## Estrutura do Projeto

A estrutura do projeto inclui:

```
pokemon-api/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── conftest.py
├── docker-compose.yml
└── README.md
```

- **`app/`**: Contém o código da aplicação FastAPI.
  - **`main.py`**: Código principal da API.
  - **`requirements.txt`**: Lista de dependências Python.
  - **`Dockerfile`**: Arquivo para construir a imagem Docker da aplicação.
  - **`tests/`**: Pasta com testes da aplicação.
    - **`conftest.py`**: Configuração do ambiente de testes.
- **`docker-compose.yml`**: Arquivo de configuração do Docker Compose.
- **`README.md`**: Documentação do projeto, como este arquivo, que fornece informações sobre configuração, uso e endpoints da API.
