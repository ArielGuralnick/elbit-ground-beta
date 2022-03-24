#!/bin/bash


echo Building imageDOCKER_BUILD_CMD="docker build -t caddy-2.4.2-alpine:latest . -f Dockerfile.alpine"
echo Executing: $DOCKER_BUILD_CMD
eval $DOCKER_BUILD_CMD

