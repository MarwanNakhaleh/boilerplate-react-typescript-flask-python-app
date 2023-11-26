# Step 1: Use a Node.js base image
FROM --platform=linux/amd64 node:18-alpine as build

# Set the working directory in the Docker container
WORKDIR /app

ENV NODE_OPTIONS=--openssl-legacy-provider

# Copy the rest of your app's source code into the container
COPY . .

# Install dependencies in the container
RUN CI=true yarn install

# Set the environment variable
ENV API_URL=https://api.branson.solutions

# Start the application
RUN yarn start

# Expose port 3000
EXPOSE 3000

# Start the React app
CMD ["yarn", "start"]
