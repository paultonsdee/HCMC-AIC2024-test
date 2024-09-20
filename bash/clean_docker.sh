#!/bin/sh

echo "Cleaning docker images ..."
if docker image prune -f; then
  docker rmi -f $(docker images -aq)
  echo "Successfully removed unused images."
else
  echo "Error removing images."
fi

echo "Cleaning docker containers ..."
if docker container prune -f; then
  docker rm -vf $(docker ps -aq)
  echo "Successfully removed stopped containers."
else
  echo "Error removing containers."
fi