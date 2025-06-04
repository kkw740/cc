from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask deployed on GCP App Engine!'

if __name__ == '__main__':
    app.run()
