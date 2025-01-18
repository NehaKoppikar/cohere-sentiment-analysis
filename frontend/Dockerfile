# # FROM node:18-bullseye-slim
# FROM node:18-alpine

# WORKDIR /app

# # Copy package.json and package-lock.json (if using npm)
# COPY package.json package-lock.json ./

# # Install dependencies
# RUN npm install
# RUN npm install axios
# RUN npm install -g rollup

# # Copy the rest of the application code
# COPY . .

# # Build the application
# RUN npm run build

# # Expose the port the app runs on
# EXPOSE 5173

# # Command to run the application
# CMD ["npm", "run", "dev"]

# Frontend Dockerfile
# ./frontend/Dockerfile
# Frontend Dockerfile
# FROM --platform=linux/amd64 node:18-alpine as builder

# WORKDIR /app

# # Copy package files
# COPY package*.json ./

# # Clear npm cache and remove existing node_modules
# RUN npm cache clean --force && \
#     rm -rf node_modules package-lock.json

# # Install dependencies with specific platform
# RUN npm install --no-optional --platform=linux --arch=x64
# RUN npm install axios

# # Copy rest of the application
# COPY . .

# Build the application
# RUN npm run build

# # Production stage
# FROM --platform=linux/amd64 nginx:alpine

# # Copy built assets from builder stage
# COPY --from=builder /app/dist /usr/share/nginx/html

# # Add nginx configuration for SPA
# RUN echo 'server { \
#     listen 80; \
#     location / { \
#         root /usr/share/nginx/html; \
#         index index.html; \
#         try_files $uri $uri/ /index.html; \
#     } \
# }' > /etc/nginx/conf.d/default.conf

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]

# Stage 1: Build
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy source code and build
COPY . .
RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine

# Copy built files from builder
COPY --from=builder /app/dist /usr/share/nginx/html

# Default NGINX port
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]