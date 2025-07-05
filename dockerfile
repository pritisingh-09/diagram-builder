FROM python:3.9-slim

# Install system dependencies (Graphviz)
RUN apt-get update && apt-get install -y graphviz

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
