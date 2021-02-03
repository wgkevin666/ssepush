### local redis
docker pull redis

### before start server run redis
docker run --name redis-lab -p 6379:6379 -d redis --rm

### use redis method
docker exec -it redis-lab /bin/bash
redis-cli
SUBSCRIBE channel channelname

### install package
pip3 install requirements.txt

### run server
gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000 --log-level=debug --log-syslog-to  udp://127.0.0.1:12201
