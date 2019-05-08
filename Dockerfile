FROM python:3.7-alpine

# Update and upgrade packages, create app user and app directory, add `app` (1337) user and group,
# set permissions for app directory, set no password for `app` user.
RUN apk update && apk upgrade
RUN apk add --no-cache g++ linux-headers sudo
RUN mkdir /app && addgroup -g 1337 -S app && adduser -u 1337 -h /app -D -S app -G app  && \
    chown -R app:app /app && chmod -R g+w /app && echo "app ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers

# Add files of the app directory inside the container.
ADD ./app /app

# Set working directory.
WORKDIR /app

# Set mandatory env variables beforehand as we are running pip operations below.
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /app

# Set user.
USER app

# Upgrade pip and install dependencies.
RUN sudo -H pip install --upgrade pip
RUN sudo -H pip install -r requirements.txt
