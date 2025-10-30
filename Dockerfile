FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
RUN echo 'Hello World' > /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
