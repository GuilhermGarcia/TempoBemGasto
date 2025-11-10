FROM nginx:stable-alpine

RUN rm -rf /usr/share/nginx/html/*

# Copia o build já existente (feito no seu PC ou unzipado no servidor)
COPY build /usr/share/nginx/html

# 🔧 Garante que nginx consegue ler tudo
RUN chown -R nginx:nginx /usr/share/nginx/html \
    && find /usr/share/nginx/html -type d -exec chmod 755 {} \; \
    && find /usr/share/nginx/html -type f -exec chmod 644 {} \;

EXPOSE 80
CMD ["nginx","-g","daemon off;"]
