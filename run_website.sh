#!/bin/bash
#uvicorn main:app --host 0.0.0.0 --port 8000 &
#echo "Server started with PID $!"

# Kill and remove any running memphis_website container
container_id=$(docker ps -q --filter ancestor=memphis_website)
if [ -n "$container_id" ]; then
  echo "Stopping and removing running memphis_website container: $container_id"
  docker stop $container_id
  docker rm $container_id
fi

docker build -t memphis_website .
docker run -d -p 8070:8000 memphis_website

