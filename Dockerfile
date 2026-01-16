# Sử dụng Python image nhẹ
FROM python:3.9-slim

WORKDIR /app

# Cài đặt Flask
RUN pip install flask

# Copy source code
COPY app.py .

# Mở port 5000
EXPOSE 5000

# Chạy app
CMD ["python", "app.py"]
