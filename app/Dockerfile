# api_pokedex/app/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
