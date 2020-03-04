# This image runs automatically a nginx server
FROM nginx
# Override default conf with our
COPY ./nginx.dev.conf /etc/nginx/nginx.conf