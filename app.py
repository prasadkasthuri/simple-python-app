from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    # Listen on all network interfaces (0.0.0.0) instead of localhost (127.0.0.1)
    app.run(host='0.0.0.0', port=5000)

