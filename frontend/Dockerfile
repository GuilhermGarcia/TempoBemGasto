# Etapa final: só servir o build pronto
FROM nginx:stable-alpine

# Remove os arquivos padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia o build já existente (feito no seu PC)
COPY build /usr/share/nginx/html

# Expõe a porta padrão do Nginx
EXPOSE 80

# Comando padrão do container
CMD ["nginx", "-g", "daemon off;"]

