from flask import Flask, render_template, request
from flask_sse import sse
import logging
import graypy

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')

my_logger = logging.getLogger('sse')
my_logger.setLevel(logging.DEBUG)
handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/user2')
def index1():
    return render_template("index2.html")
@app.route('/user3')
def index2():
    return render_template("index3.html")

# cheannel 123
@app.route('/hello', methods = ['POST'])
def publish_hello():
    json_data = request.json
    message = json_data["message"]
    sse.publish({"message": message}, type='greeting', retry=4500, channel="123")
    return "Message sent!"

# channel 456
@app.route('/user', methods = ['POST'])
def publish_hello1():
    json_data = request.json
    message = json_data["message"]
    # channel = json_data["user_id"]
    # channel is user_id
    sse.publish({"message": message}, type='greeting2', channel="456")
    return "Message sent!!!"

# brodcast notifi
@app.route('/', methods = ['POST'])
def publish_alluser():
    # print(request.method)
    # print(request.args)
    # message = request.args.get('message')
    # print(request.args.get("message"))
    json_data = request.json
    message = json_data["message"]
    sse.publish({"message": message }, type='postmessage')
    return "brodcast OK!!"
    my_logger.debug('publish_alluser post')
    try:
        unknow_function()
    except NameError:
        my_logger('The "unknow_function" raised an error')



if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.info')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
