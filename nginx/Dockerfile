# instalamos una versión LITE de nginx que se 
# encuentra disponible en docker-hub al igual que con
# la de python
FROM nginx:1.15.0-alpine

# eliminamos el archivo de configuración por defecto de nginx
RUN rm /etc/nginx/conf.d/default.conf
# y copiamos el archivo de conf que creamos, dentro de docker
COPY nginx.conf /etc/nginx/conf.d