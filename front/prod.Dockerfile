FROM node:latest as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

# This image runs automatically a nginx server
FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
# Override default conf with our
COPY nginx.prod.conf /etc/nginx/nginx.conf