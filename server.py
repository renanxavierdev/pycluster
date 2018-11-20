from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import json
from io import StringIO
import time
import psutil
from threading import Thread
import socket
import pusher

pusher_client = pusher.Pusher(
  app_id='652059',
  key='f8dca6cc86dc0ff772f8',
  secret='020c5721ffa64f199c65',
  cluster='us2',
  ssl=True
)


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}

    js = json.loads(request.data)
    keys 	= js['params'][0]['keys'].split(", ")
    words 	= js['params'][0]['words']

    json_test={}
    word_count = {}
    start = time.time()
    for key in keys:
    	for word in words:
    		if key == word:
    			if word not in word_count:
    				word_count[word] = 1
    			else:
    				word_count[word] = word_count[word] + 1


    end = time.time()
    t = end-start
    json_test = json.dumps({'keys':word_count, 'timer':t})
    print json_test
    return Response(json_test, mimetype='application/json')

def cpuUsage():
	while True:
		time.sleep(2)
		pusher_client.trigger(socket.gethostbyname(socket.gethostname()), 'usage', {'message': {'cpu':psutil.cpu_percent()} })

if __name__ == '__main__':
    Thread(target=cpuUsage, args=[]).start()
    run_simple(socket.gethostbyname(socket.gethostname()), 4000, application)
