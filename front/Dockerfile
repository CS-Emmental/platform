# base image
FROM node:8.10.0-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./

RUN npm install

EXPOSE 8080

CMD [ "npm", "run", "serve"]