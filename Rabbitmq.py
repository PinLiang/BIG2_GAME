import pika
import simplejson as json

def createqueue(name):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue=name)
	connection.close()

def whointhegame(playerlist, user):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":5,"neisae":user})
	for a in range(len(playerlist)):
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()

def wholeavethegame(playerlist, user):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":6,"neisae":user})
	for a in range(len(playerlist)):
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()

def sendnewtablemessage(lobbyplayer, roomtitle):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":4,"yoney":roomtitle,"nike":3})
	for a in range(len(lobbyplayer)):
		channel.basic_publish(exchange='',routing_key=lobbyplayer[a],body=data)
	connection.close()