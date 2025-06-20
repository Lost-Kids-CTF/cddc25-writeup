#!/bin/bash

docker rm -f oldgame
docker run -d -p 6666:6666 --name oldgame --restart unless-stopped --privileged oldgame