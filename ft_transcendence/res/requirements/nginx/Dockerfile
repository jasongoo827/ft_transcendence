FROM nginx:1.25-alpine

RUN apk add openssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/server_pkey.pem -out /etc/ssl/certs/server.crt -subj "/C=/ST=/L=/O=/CN="

COPY fe /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
