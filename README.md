### local redis
docker pull redis

### before start server run redis
docker exec -it redis-lab /bin/bash

### run server
gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000
