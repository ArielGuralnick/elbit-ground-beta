#!/bin/bash


echo Building image:
echo Executing: docker build -t caddy-2.4.2-alpine:latest .
docker build -t caddy-2.4.2-alpine:latest .

