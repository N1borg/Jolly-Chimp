FROM python:3.12

# Prevents Python from writing .pyc files and ensures logs are not buffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy all application files, including requirements.txt and config.json
COPY . /app/

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    python3-dev default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Default command to run the application
CMD ["python", "scraper.py"]
