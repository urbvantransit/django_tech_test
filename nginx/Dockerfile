#
# Docker image for nginx
#
FROM nginx

EXPOSE 80 443

RUN mkdir -p /logs
COPY nginx.conf /etc/nginx/
COPY urbvan.conf /etc/nginx/sites-enabled/
