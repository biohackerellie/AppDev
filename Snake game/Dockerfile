FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install pygame

EXPOSE 6080 5900

COPY snake.py /

ENTRYPOINT ["xvfb-run", "-a", "python3", "snake.py"]