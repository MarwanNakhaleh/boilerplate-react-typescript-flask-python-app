# Step 1: Use a Node.js base image
FROM node:18-alpine as build

# Set the working directory in the Docker container
WORKDIR /app

# Copy the package.json and yarn.lock files into the container
COPY package.json yarn.lock ./

# Install dependencies in the container
RUN yarn install --frozen-lockfile

# Copy the rest of your app's source code into the container
COPY . .

# Set the environment variable
ENV API_URL=https://api.branson.solutions

# Build the application
RUN yarn build

# Step 2: Use a smaller base image to run the application
FROM nginx:alpine

# Copy the build from the previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx and serve the application
CMD ["nginx", "-g", "daemon off;"]
