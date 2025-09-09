FROM ubuntu:latest
LABEL authors="juuzou"

ENTRYPOINT ["top", "-b"]