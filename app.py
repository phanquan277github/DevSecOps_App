from flask import Flask
import os

app = Flask(__name__)

# SECURITY VULNERABILITY: Hardcoded AWS Credentials (SonarQube SEVERITY: CRITICAL)
AWS_ACCESS_KEY_ID = "AKIA5QY72W3V9L8M1Z4K" 
AWS_SECRET_ACCESS_KEY = "z8a9s8d7f6g5h4j3k2l1m0n9b8v7c6x5z4a3s2d1"

DB_PASSWORD = "admin_password_123"

@app.route('/')
def hello():
    return f"Hello DevSecOps TestV2 CI/CD Pipeline! Database password is: {DB_PASSWORD}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
