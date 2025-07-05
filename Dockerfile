# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8080

# Use environment variable PORT (required by Render), with fallback
ENV PORT 8080

# Set Streamlit to run using the environment PORT
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
