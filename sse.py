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
    sse.publish({"message": "hello kevin"}, type='greeting', retry=4500, channel="123")
    return "Message sent!"

@app.route('/hello1')
def publish_hello1():
    sse.publish({"message": "hello david"}, type='greeting', retry=4500, channel="456")
    return "Message sent!!!"

@app.route('/user', methods = ['POST','GET'])
def publish_user():
    print(request.method)
    print(request.args)
    message = request.args.get('message')
    print(request.args.get("msg"))
    sse.publish({"message": message }, type='postmessage')
    return "channel"