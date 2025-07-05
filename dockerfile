# Use lightweight Python base
FROM python:3.10-slim

# Install system dependencies (including Graphviz)
RUN apt-get update && apt-get install -y graphviz

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose required port
EXPOSE 8000

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.enableCORS=false"]
