FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy your requirements file
COPY requirements.txt .

# Install dependencies (including psycopg2-binary)
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Command to run your app (adjust as needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
