FROM nginx:1.27-alpine

# Удаляем дефолтный конфиг
RUN rm /etc/nginx/conf.d/default.conf

# Кладём наш конфиг
COPY nginx.conf /etc/nginx/conf.d/app.conf
