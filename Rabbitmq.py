import pika
import DealCard
import Big2
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

def whointhetable(playerlist, user):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":7,"iaen":user})
	for a in range(len(playerlist)):
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()

def updatetablestillneed(lobbyplayer, roomtitle, need):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":8,"yoney":roomtitle,"nike":need})
	for a in range(len(lobbyplayer)):
		channel.basic_publish(exchange='',routing_key=lobbyplayer[a],body=data)
	connection.close()

def dealercard(playerlist, roomtitle):
	cards = DealCard.dealcard()
	table = Big2.Tables.query.filter_by(titles=roomtitle).first()
	table.cards1 = ','.join(cards[0])
	table.cards2 = ','.join(cards[1])
	table.cards3 = ','.join(cards[2])
	table.cards4 = ','.join(cards[3])
	Big2.db.session.commit()
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	for a in range(4):
		data = json.dumps({"revent":1,"cards":cards[a],"dropcard":[playerlist[cards[4]],playerlist[(cards[4]+1)%4],playerlist[(cards[4]+2)%4],playerlist[(cards[4]+3)%4]]})
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()

def updatetablesdisappear(lobbyplayer,roomtitle):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":9,"yoney":roomtitle})
	for a in range(len(lobbyplayer)):
		channel.basic_publish(exchange='',routing_key=lobbyplayer[a],body=data)
	connection.close()

def dropcardbrocast(playerlist,dropuser,cards):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":2,"dropuser":dropuser,"cards":cards,"pdcchance":playerlist[0]})
	for a in range(len(playerlist)):
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()

def whowinthegame(playerlist):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	data = json.dumps({"revent":10,"winner":playerlist[3]})
	for a in range(len(playerlist)):
		channel.basic_publish(exchange='',routing_key=playerlist[a],body=data)
	connection.close()