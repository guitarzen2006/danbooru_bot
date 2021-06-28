# Danbooru Bot - A simple anime/manga pic grabber for Discord

This is one of my first attempts at creating a chat bot for discord. As a fan of various anime and manga I have created a simple chatbot for discord to pull pictures from the [safebooru.donmai.us](https://safebooru.donmai.us) wiki which has a simple API and thousands of posts from various professional and amatuer artists. Documentation on their API can be found here: https://safebooru.donmai.us/wiki_pages/help:api 

Please note that safebooru is a default safe search, the actual site is [danbooru.donmai.us](https://danbooru.donmai.us). However the content at that site is too explicit for my taste and I do not recommend it for general use.

# How I Run the Chatbot

The chatbot's script is ran as a docker container on a virtualized device in the cloud. I am running danbooru_bot as a docker container on a server in the cloud. This is a high level overiview of how I build and running the docker container.

1. First build the danbooru_bot docker container. This is ran in the same file that the 'Dockerfile' is found in.

```
docker build -t danbooru_bot:latest .
```
2. Verify that the Docker container has been built. You can check your local image inventory.
```
docker images
```
3. Run the image. You will note that I am running my container in the background and using the docker syslog plugin to send all logging to the host /var/log/syslog folder. The logging for this application by default will print logs to stdout and a file named app.log within the container.
```
docker run --log-driver syslog danbooru_bot:latest &
```
4. Verify that the container is running.
```
docker ps -a
```
You should similar output.
```
> sudo docker ps -a
CONTAINER ID   IMAGE         COMMAND                 CREATED             STATUS                         PORTS     NAMES
46241833e46a   d078b         "python ./app/bot.py"   55 minutes ago      Up 55 minutes                            jolly_khayyam
```