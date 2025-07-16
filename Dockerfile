# Use Python 3.11 as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]

