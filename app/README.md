# SimpleTimeService

SimpleTimeService is a lightweight microservice that returns the current timestamp and the visitor's IP address in JSON format.

## Features
- Returns current timestamp (UTC)
- Captures client IP address
- Lightweight and secure containerized setup

## Requirements
- Docker installed

## Setup

### 1. Build the Docker Image
```sh
docker build -t simple-time-service .
```
### 2. Run the Container
```sh
docker run -p 5000:5000 simple-time-service
```
### 3. Access the Service
Visit http://localhost:5000/ in a browser or use:
curl http://localhost:5000/

