from flask import Flask
from prometheus_client import generate_latest, Counter, Histogram
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

# Sample metric (optional)
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        return "Hello from URL Shortener!"

# ✅ This is the important part
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
