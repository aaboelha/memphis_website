#!/bin/bash
#uvicorn main:app --host 0.0.0.0 --port 8000 &
#echo "Server started with PID $!"

docker build -t memphis_website .
docker run -d -p 8070:8000 memphis_website

