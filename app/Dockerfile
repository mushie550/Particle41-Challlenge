# Use a minimal base image
FROM python:3.9-slim

# Create a non-root user
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

# Copy necessary files to keep the image lightweight
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

