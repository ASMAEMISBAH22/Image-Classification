FROM python:3.10-slim

# Install system dependencies required by TensorFlow
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY app/ ./app

# Create directory for uploads (make it a volume for persistence)
RUN mkdir temp_uploads
VOLUME ["/app/temp_uploads"]

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to start FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
