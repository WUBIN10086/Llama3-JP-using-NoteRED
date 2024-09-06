# 使用官方的 Python 基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制当前文件夹内容到容器内
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 API 的端口
EXPOSE 8080

# 运行 llama_api.py
CMD ["python", "llama_api.py"]
