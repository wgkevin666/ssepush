from flask import Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/user2')
def index1():
    return render_template("index2.html")
@app.route('/user3')
def index2():
    return render_template("index3.html")

@app.route('/hello', methods = ['POST'])
def publish_hello():
    json_data = request.json
    message = json_data["message"]
    sse.publish({"message": message}, type='greeting', retry=4500, channel="123")
    return "Message sent!"

@app.route('/user', methods = ['POST'])
def publish_hello1():
    json_data = request.json
    message = json_data["message"]
    channel = json_data["user_id"]
    # channel is userid
    sse.publish({"message": message}, type='greeting2', channel="456")
    return "Message sent!!!"

@app.route('/', methods = ['POST'])
def publish_alluser():
    # print(request.method)
    # print(request.args)
    # message = request.args.get('message')
    # print(request.args.get("message"))
    json_data = request.json
    message = json_data["message"]
    sse.publish({"message": message }, type='postmessage')
    return "channel"