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
```sh
curl http://localhost:5000/
```
Expected JSON response:
```sh
{
  "timestamp": "2025-03-28T12:34:56.789123",
  "ip": "127.0.0.1"
}
```
### 4. Pull from DockerHub
```sh
docker pull musharraf1716/simple-time-service:latest
docker run -p 5000:5000 musharraf1716/simple-time-service:latest
```


