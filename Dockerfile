# Use official Python image compatible with your Apple M3 chip
FROM python:3.11-slim

# Set working directory in container
WORKDIR /src/app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "src.inference_service:app", "--host", "0.0.0.0", "--port", "8000"]
