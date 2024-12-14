# FROM ubuntu:focal # change this if access slowly
FROM hub.geekery.cn/ubuntu:focal

COPY sources.list /etc/apt/sources.list

# 设置环境变量，防止交互提示
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y  --no-install-recommends libfftw3-dev libconfig-dev libasound2-dev libpulse-dev libxcursor-dev \
    x11-apps \
    libgtk2.0-0 \
    libx11-6 \
    libxext6 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    xauth \
    x11-utils \
    python3-opencv \
    libsm6 \
    libxext6 \
    libxrender-dev \
    sudo

RUN rm -rf /var/lib/apt/lists/*

RUN useradd --create-home odas

# give odas user root priviledge
USER root
RUN echo "odas ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/odas \
    && chmod 0440 /etc/sudoers.d/odas


USER odas
# COPY --chown=odas . .

ENV PATH="/home/odas/.local/bin:$PATH"

WORKDIR /app

CMD ["tail","-f", "/dev/null"]
