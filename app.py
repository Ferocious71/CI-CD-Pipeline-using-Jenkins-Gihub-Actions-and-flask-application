from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def staging():
    return "This is the staging environment!"


def home():
    return "Hello! Flask App Running Successfully."

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port, debug=True)
