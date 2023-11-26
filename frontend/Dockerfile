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

# Build the application
RUN yarn build

# Step 2: Use a smaller base image to run the application
FROM nginx:alpine

# Copy the build from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx and serve the application
CMD ["nginx", "-g", "daemon off;"]
