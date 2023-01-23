# fetch the base docker image
FROM ubuntu:latest

# mises à jour
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip

# creation working directory inside the container
WORKDIR /code

# recopier mon app to the container
ADD . /code/

# install dependencies & pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# ignore l'alerte de conflit
ENV PIP_ROOT_USER_ACTION=ignore
# make my app accessible for others
EXPOSE 5000

# maintain in a running state (executable)
CMD ["python3", "/code/app.py"]