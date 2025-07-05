# Dockerfile

FROM python:3.10-slim

# Install Graphviz
RUN apt-get update && apt-get install -y graphviz

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit runs on port 8501
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
