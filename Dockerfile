FROM python:3.11-slim

WORKDIR /app

COPY offline_packages /app/offline_packages
COPY requirements.txt .

# 1. 替换 APT 源为阿里云 Debian 12 (Bookworm) 源
RUN echo "deb http://mirrors.aliyun.com/debian/ bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ bookworm-updates main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security/ bookworm-security main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    rm -f /etc/apt/sources.list.d/debian.sources
# 2. 配置 pip 使用阿里云源
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip config set global.trusted-host mirrors.aliyun.com

# 不从网络安装，只从离线包安装
RUN pip install --no-cache-dir -r requirements.txt \
    --find-links /Users/lang/Documents/2026_project/offline_packages \
    --no-index

COPY . .

CMD ["pytest", "tests/", "-v"]