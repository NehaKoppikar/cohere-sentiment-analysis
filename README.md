# Movie Review Sentiment Analysis

A web application that analyzes the sentiment of movie reviews using Cohere's LLM API. The application consists of a ReactJS frontend and a FastAPI backend, containerized with Docker and deployed on the GCP Compute Engine.

<br>

[Deployed Application URL](http://34.173.57.156/)
<br>
Screenshot
![image](https://github.com/user-attachments/assets/093fe1dc-5617-451b-8014-2dd9d73b0d52)


## Architecture Overview

The application follows a microservices architecture with the following components:

- **Frontend**: React application that provides the user interface for submitting movie reviews and displaying sentiment analysis results
- **Backend**: FastAPI service that interfaces with Cohere's API to perform sentiment analysis
- **API Integration**: Cohere's LLM API for natural language processing and sentiment classification
- **Docker**: Containerization of both frontend and backend services
- **Nginx**: Reverse proxy to handle routing and serve the application
  ![image](https://github.com/user-attachments/assets/5190ceba-2861-4250-8b78-44f173f3ec79)


## Prerequisites

- Docker and Docker Compose
- Cohere API key (get it from [Cohere Dashboard](https://dashboard.cohere.com/api-keys))
- GCP account with Compute Engine access (for deployment)

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/NehaKoppikar/cohere-sentiment-analysis.git
cd cohere-sentiment-analysis
```

2. Create a `.env` file in the root directory:
```env
cohere_api=your_api_key_here
CORS_ORIGINS=http://localhost:5173
```

3. Start the application using Docker Compose:
```bash
docker compose up -d --build
```

4. Access the application:
- Frontend: http://localhost:5173
- Backend testing: http://localhost:8080/docs (FastAPI Swagger UI) <br>
The frontend looks something like this:
![image](https://github.com/user-attachments/assets/ad4dadbb-6842-488a-9914-0c6395f839ef)


## Backend Endpoints

The backend provides two endpoints:

1. Health Check:
   - URL: `GET /health`
   - Response: `{"status": "healthy"}`
    <img width="1498" alt="backend_health_check" src="https://github.com/user-attachments/assets/bf59d1ef-5984-4579-b423-5a5bcd5d9634" />


2. Sentiment Analysis:
   - URL: `POST /sentiment-analysis`
   - Content-Type: `application/x-www-form-urlencoded`
   - Form Parameter: `text` (the movie review text)
   - Response Example:
     ```json
     {
       "sentiment": "Positive",
       "confidence": 95.5,
       "message": "This seems like a positive review."
     }
     ```
     <img width="1492" alt="backend_sentiment_analysis_prediction" src="https://github.com/user-attachments/assets/605e81d6-198d-402f-be6b-adc334448e96" />


## Deployment Steps

1. SSH into your GCP Compute Engine instance:
```bash
gcloud compute ssh your-instance-name
```

2. Install Docker and Docker Compose:
```bash
# Install Docker
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

3. Clone the repository and set up the environment:
```bash
git clone https://github.com/NehaKoppikar/cohere-sentiment-analysis.git
cd cohere-sentiment-analysis
cp .env.example .env
# Edit .env with your Cohere API key
nano .env
```

4. Install and configure Nginx:
```bash
sudo apt install nginx -y
sudo nano /etc/nginx/sites-available/app.conf
# Copy the Nginx configuration provided in the repository
sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

5. Start the application:
```bash
docker compose up -d --build
```

## Troubleshooting

1. If containers fail to start:
   ```bash
   docker compose logs
   ```

2. Common issues:
   - Verify Cohere API key is correctly set in `.env`
   - Check if ports 5173 and 8080 are available
   - Ensure Docker service is running
   - Verify all containers are up: `docker compose ps`

3. For deployment issues:
   - Check GCP firewall rules for ports 80, 5173, and 8080
   - Verify Nginx configuration
   - Check application logs: `docker compose logs frontend` or `docker compose logs backend`

## Security Notes

- The Cohere API key is stored in the `.env` file (not committed to the repository)
- CORS is configured to allow only localhost origins for development
- Nginx is configured with security headers
- Input validation is implemented on the backend