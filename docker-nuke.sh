#!/bin/bash

docker container stop $(docker container ls -aq)

docker container rm $(docker container ls -aq)

docker image prune -a

docker volume prune

docker network prune
