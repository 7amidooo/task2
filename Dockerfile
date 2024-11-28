# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY monitoring.py .

# Install any necessary dependencies (optional)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts (interactive mode)
CMD ["python", "monitoring.py"]
