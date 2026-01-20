from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# --- CONFIG ---
AWS_ACCESS_KEY_ID = "AKIA5QY72W3V9L8M1Z4K" 
AWS_SECRET_ACCESS_KEY = "z8a9s8d7f6g5h4j3k2l1m0n9b8v7c6x5z4a3s2d1"
DB_PASSWORD = "admin_password_123"

@app.route('/')
def hello():
    return f"""
    <h1>Vulnerable App - DAST Demo</h1>
    <p>Database password is: {DB_PASSWORD}</p>
    <p><a href="/search?query=test">Go to Vulnerable Search</a></p>
    """

# --- VULNERABLE ENDPOINT FOR ZAP TO ATTACK ---
@app.route('/search')
def search():
    query = request.args.get('query', '')

    # LỖI 1: Reflected XSS (In trực tiếp input ra màn hình không qua lọc)
    # ZAP sẽ thử chèn <script>alert(1)</script> vào đây
    template = f"""
    <h2>Search Results</h2>
    <p>You searched for: <b>{query}</b></p> 
    <form><input name="query"><input type="submit" value="Search"></form>
    """

    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
