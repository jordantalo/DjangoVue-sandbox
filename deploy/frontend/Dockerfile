# Pull base image
FROM node:26-bookworm

# Set work directory
WORKDIR /app

# Install dependencies
COPY srcs/frontend/package*.json .
RUN npm install

# Copy project
COPY srcs/frontend .

EXPOSE 5173
