#!/bin/bash

docker build -t snake:latest . && \

docker run --name snake -p 6080:6080 -p 5900:5900 snake:latest
