from flask import Flask
import os

app = Flask(__name__)

# LỖI BẢO MẬT 1: Hardcoded Password (SonarQube sẽ bắt lỗi này)
DB_PASSWORD = "admin_password_123"

@app.route('/')
def hello():
    return f"Hello DevSecOps TestV2 CI/CD Pipeline! Database password is: {DB_PASSWORD}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
