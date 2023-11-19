# Use an Alpine Python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

EXPOSE 8000

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .

# Specify the command to run on container start
CMD [ "python", "./api.py"]
