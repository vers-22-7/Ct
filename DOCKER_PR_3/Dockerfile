FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /data
WORKDIR /data
CMD ffmpeg -i /sources/image.jpg -vf "scale=iw*0.5:ih*0.5" output.jpg
