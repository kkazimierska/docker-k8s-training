# our base image
FROM alpine:3.15

# Install python and pip
RUN apk add --update py3-pip

# install Python modules needed by the Python app
# Layering system - copy before you run pip install - then remembers the cache
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
# COPY templates/index.html /usr/src/app/templates/
# COPY templates/dogs.html /usr/src/app/templates/
# Use volume instead of copying the templates - we could modify the templates and changes will be reflected directly
# Local file requirements is used for local dev not publisihing images.

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python3", "/usr/src/app/app.py"]
