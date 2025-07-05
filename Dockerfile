# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY . .

# Expose the port (optional, but good practice)
EXPOSE 8080

# Let Render inject the PORT environment variable
# Default to 8080 for local testing
ENV PORT=8080

# Correct CMD without quotes
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
