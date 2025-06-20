#!/bin/sh

docker rm -f oldgame
docker rmi -f oldgame

docker build -t oldgame .