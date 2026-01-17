from flask import Flask
import os

app = Flask(__name__)

# SECURITY VULNERABILITY: Hardcoded AWS Credentials (SonarQube SEVERITY: CRITICAL)
AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDEF" 
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/')
def hello():
    return f"Hello DevSecOps TestV2 CI/CD Pipeline! Database password is: {DB_PASSWORD}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
