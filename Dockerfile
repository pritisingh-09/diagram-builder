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

# Expose the port Render will assign
EXPOSE 8000

# Run your Streamlit app with the Render-assigned port
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.enableCORS=false"]
