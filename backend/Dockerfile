# # Use a lightweight Python image
# FROM python:3.10-slim-bullseye

# # Set the working directory in the container
# WORKDIR /app

# # Copy requirements.txt into the container
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the backend code
# COPY . .

# # Expose the backend port
# EXPOSE 8000

# # Run the FastAPI app with uvicorn
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Backend Dockerfile
# ./backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .
EXPOSE 8080

# Start the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]