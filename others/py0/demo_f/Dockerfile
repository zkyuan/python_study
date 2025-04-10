FROM ubuntu:latest

# 更改Ubuntu的源为阿里云的源
RUN sed -i 's@archive.ubuntu.com/@/mirrors.aliyun.com/@g' /etc/apt/sources.list && apt-get update

# 安装必要的软件包
RUN apt-get install -y coturn python3 python3-pip redis-server python3-venv

# 创建虚拟环境
RUN python3 -m venv /app/venv

COPY requirements.txt .

# 激活虚拟环境并安装Python依赖
RUN /app/venv/bin/pip install --upgrade pip
RUN /app/venv/bin/pip install fastapi uvicorn langchain_core langchain_openai langchain langchain_community openai redis google-search-results
RUN /app/venv/bin/pip install -r  requirements.txt

# 安装NLTK
RUN /app/venv/bin/pip install nltk

COPY nltk_data /app/venv/nltk_data

# 复制配置文件
COPY turnserver.conf /etc/turnserver.conf
COPY redis.conf /etc/redis/redis.conf

# 设置数据卷
VOLUME /data

# 设置工作目录
WORKDIR /app

# 复制代码
COPY . /app

ENV NLTK_DATA /app/venv/nltk_data

# 暴露端口
EXPOSE 8000 3478 6379

# 启动服务
CMD ["sh", "-c", "turnserver -c /etc/turnserver.conf --listening-ip=0.0.0.0 --listening-port=3478 & redis-server /etc/redis/redis.conf --protected-mode no & sleep 3 && /app/venv/bin/uvicorn server:app --host 0.0.0.0 --port 8000"]