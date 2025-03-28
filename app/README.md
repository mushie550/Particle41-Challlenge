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

