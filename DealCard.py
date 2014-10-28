import random
import simplejson as json

def dealcard(usernember):
	# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	# channel = connection.channel()
	player1=[]
	player2=[]
	player3=[]
	player4=[]
	poker = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13']
	#One player have 4 big 2 cards re-deal
	while True:
		random.shuffle(poker)
		for a in range(len(poker)):
			if a < 13:
				player1.append(poker[a])
			elif a < 27:
				player2.append(poker[a])
			elif a < 39:
				player3.append(poker[a])
			elif a < 52:
				player4.append(poker[a])
		if (checkhave4big2(player1) and checkhave4big2(player2) and checkhave4big2(player3) and checkhave4big2(player4)):
			break
		player1=[]
		player2=[]
		player3=[]
		player4=[]

	# for a in range(len(usernember)):
	# 	channel.basic_publish(exchange='',routing_key=usernember[a],body=playerlist[a] + ' into the Room.')
	# connection.close()
	data = {'cards':player1}
	print json.dumps(data)
	print player2
	print player3
	print player4

def checkhave4big2(playercard):
	checkpoint = 0
	if 's2' in playercard:
		checkpoint += 1
	if 'h2' in playercard:
		checkpoint += 1
	if 'c2' in playercard:
		checkpoint += 1
	if 'd2' in playercard:
		checkpoint += 1
	if checkpoint == 4:
		return False
	else:
		return True

dealcard(1)