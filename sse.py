from flask import Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "hello kevin"}, type='greeting', retry=4500,channel="123")
    return "Message sent!"

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "hello kevin"}, type='greeting', retry=4500,channel="456")
    return "Message sent!"

@app.route('/hello1', methods = ['POST'])
def publish_user():
    message = request.args.get("msg")
    print(request.args)
    print(request.args.get("msg"))
    sse.publish({"message": message}, type='greeting',)
    return "channel"