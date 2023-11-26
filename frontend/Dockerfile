# Step 1: Use a Node.js base image
FROM node:18-alpine as build

# Set the working directory in the Docker container
WORKDIR /app

# Copy the app's source code into the container
COPY . .

# Install dependencies in the container
RUN yarn install

# Set the environment variable
ENV API_URL=https://api.branson.solutions

# Start Nginx and serve the application
CMD ["yarn", "start"]
