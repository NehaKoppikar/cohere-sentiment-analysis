# Build stage
FROM node:18-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install
# RUN npm install axios

# Copy source code
COPY . .

# Build the app (use the Docker-specific config)
RUN cp vite.config.docker.js vite.config.js && npm run build

# # Production stage
# FROM nginx:alpine

# # Copy the built files from build stage
# COPY --from=build /app/dist /usr/share/nginx/html

# # Copy nginx configuration
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 5173

# CMD ["nginx", "-g", "daemon off;"]
CMD ["npm", "run", "dev"]