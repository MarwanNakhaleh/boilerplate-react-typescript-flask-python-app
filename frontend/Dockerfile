# Step 1: Use a Node.js base image
FROM --platform=linux/amd64 node:lts as build

# Set the working directory in the Docker container
WORKDIR /app

# Define the arguments
ARG API_URL
ARG REACT_APP_GOOGLE_CLIENT_ID

# Set the environment variables
ENV YARN_ENABLE_IMMUTABLE_INSTALLS=false
ENV API_URL=${API_URL}
ENV REACT_APP_GOOGLE_CLIENT_ID=${REACT_APP_GOOGLE_CLIENT_ID}
ENV NODE_OPTIONS=--openssl-legacy-provider

# Copy the rest of your app's source code into the container
COPY package.json yarn.lock ./

# Github actions didn't appear to save my information correctly so I'm doing this madness
RUN touch .env
RUN echo "REACT_APP_GOOGLE_CLIENT_ID=${REACT_APP_GOOGLE_CLIENT_ID}" >> .env
RUN echo "" >> .env
RUN echo "API_URL=${API_URL}" >> .env

# Install dependencies in the container
RUN CI=true yarn install

COPY . ./

RUN yarn build

# Stage 2: Set up Nginx to serve the app
FROM --platform=linux/amd64 nginx:alpine

# Copy the build output to replace the default nginx contents.
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 to the outside once the container has launched
EXPOSE 80

# Start Nginx and keep it running
CMD ["nginx", "-g", "daemon off;"]