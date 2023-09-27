#http server for hostinf static pages
FROM nginx
ENV AUTHOR=Docker
# Setting root directory that we will work inside the container
WORKDIR /usr/share/nginx/html
COPY Hello_docker.html /usr/share/nginx/html
# sed replace the value of variable Docker - deamon off - wont be running on the background
CMD cd /usr/share/nginx/html && sed -e s/Docker/"$AUTHOR"/ Hello_docker.html > index.html ; nginx -g 'daemon off;'

#command executes when run