# Use an Alpine Python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD [ "python", "./api.py" ]
