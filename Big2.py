import os
import time
from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.sqlalchemy import SQLAlchemy
from threading import Thread
import simplejson as json
import random
import pika
import Rabbitmq
import DealCard

parser = reqparse.RequestParser()
parser.add_argument('user', type=str)
print parser
app = Flask(__name__)
api = restful.Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/big2'
db = SQLAlchemy(app)

playerlist=[]

class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(45, u'utf8_unicode_ci'))
	password = db.Column(db.String(45, u'utf8_unicode_ci'))
	create_date = db.Column(db.Date)
	status = db.Column(db.Integer)

class Tables(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titles = db.Column(db.String(45))
	player1 = db.Column(db.String(45))
	player2 = db.Column(db.String(45))
	player3 = db.Column(db.String(45))
	player4 = db.Column(db.String(45))
	permission = db.Column(db.String(45))
	check1 = db.Column(db.Integer)
	check2 = db.Column(db.Integer)
	check3 = db.Column(db.Integer)
	check4 = db.Column(db.Integer)
	remind1 = db.Column(db.Integer)
	remind2 = db.Column(db.Integer)
	remind3 = db.Column(db.Integer)
	remind4 = db.Column(db.Integer)
	status = db.Column(db.Integer)
	cards1 = db.Column(db.String(45, u'utf8_unicode_ci'))
	cards2 = db.Column(db.String(45, u'utf8_unicode_ci'))
	cards3 = db.Column(db.String(45, u'utf8_unicode_ci'))
	cards4 = db.Column(db.String(45, u'utf8_unicode_ci'))


#API 1. Create Account
class createaccount(restful.Resource):
	def post(self):
		confirm = request.get_json(force = True)
		player = Player.query.limit(1).all()
		if not player:
			t = time.time()
			db.session.add(Player(username=confirm['iaen'],password=confirm['eacea'],create_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))))
			db.session.commit()
			Rabbitmq.createqueue(confirm['iaen'])
			return {'hevent':1}, 201
		else:
			i = Player.query.order_by(Player.id.desc()).first()
			player = Player.query.filter_by(username=confirm['iaen']).first()
			if player is None:
				t = time.time()
				db.session.add(Player(id = i.id+1, username=confirm['iaen'],password=confirm['eacea'],create_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))))
				db.session.commit()
				Rabbitmq.createqueue(confirm['iaen'])
				return {'hevent':1}, 201
			else:
				return {'hevent':2}, 201

#API 2. Authentication Account
class authentication(restful.Resource):
	def post(self):
		playerlist = []
		tablename = []
		a = []
		confirm = request.get_json(force = True)
		player = Player.query.filter_by(username=confirm['iaen']).first()
		if player is None:
			return {'hevent':2}
		else:
			if confirm['eacea'] != player.password:
				return {'hevent':2}
			else:
				lobbyplayer = Player.query.filter_by(status=1).all()
				for i in range(len(lobbyplayer)):
					playerlist.append(lobbyplayer[i].username)
				Rabbitmq.createqueue(player.username)
				player.status = 1
				db.session.commit()
				Rabbitmq.whointhegame(playerlist, confirm['iaen'])
				tables = Tables.query.limit(1).all()
				if not tables:
					return {'tables':[],'hevent':1}
				else:
					a.append(Tables.query.order_by(Tables.titles).all())
					for b in range(len(a[0])):
						tablename.append(a[0][b].titles)
						#print a[0][b].titles
					return {'tables':tablename,'hevent':1}

#API 4. User leave the game
class userleavegame(restful.Resource):
	def post(self):
		playerlist = []
		confirm = request.get_json(force = True)
		player = Player.query.filter_by(username=confirm['iaen']).first()
		if confirm['eacea'] != player.password:
			return {'hevent':2}
		else:
			player.status = 0
			db.session.commit()
			lobbyplayer = Player.query.filter_by(status=1).all()
			for i in range(len(lobbyplayer)):
				playerlist.append(lobbyplayer[i].username)
			Rabbitmq.wholeavethegame(playerlist, confirm['iaen'])
			return {'hevent':1}

#API 5. Create table
class createtable(restful.Resource):
	def post(self):
		playerlist = []
		confirm = request.get_json(force = True)
		player = Player.query.filter_by(username=confirm['iaen']).first()
		if confirm['eacea'] != player.password:
			return {'hevent':2}
		else:
			tables = Tables.query.limit(1).all()
			if not tables:
				player.status = 2
				db.session.add(Tables(titles=confirm['taeina'],player1=confirm['iaen'],player2="empty",player3="empty",player4="empty",permission="empty",check1=0,check2=0,check3=0,check4=0,remind1=0,remind2=0,remind3=0,remind4=0,status=0))
				db.session.commit()
				player = Player.query.filter_by(status=1).all()
				for a in range(len(player)):
					playerlist.append(player[a].username)
				Rabbitmq.sendnewtablemessage(playerlist, confirm['taeina'])
				return {"hevent":1}
			else:
				tname = Tables.query.filter_by(titles=confirm['taeina']).first()
				if tname is None:
					i = Tables.query.order_by(Tables.id.desc()).first()
					player.status = 2
					db.session.add(Tables(id = i.id+1,titles=confirm['taeina'],player1=confirm['iaen'],player2="empty",player3="empty",player4="empty",permission="empty",check1=1,check2=0,check3=0,check4=0,remind1=0,remind2=0,remind3=0,remind4=0,status=0))
					db.session.commit()
					player = Player.query.filter_by(status=1).all()
					for a in range(len(player)):
						playerlist.append(player[a].username)
					Rabbitmq.sendnewtablemessage(playerlist, confirm['taeina'])
					return {'hevent':1}
				else:
					return {'hevent':3}

#API 6. User into the tables
class intothetables(restful.Resource):
	def post(self):
		playerlist = []
		lobbylist = []
		confirm = request.get_json(force = True)
		player = Player.query.filter_by(username=confirm['iaen']).first()
		if confirm['eacea'] != player.password:
			return {'hevent':2}
		table = Tables.query.filter_by(titles=confirm['yoney']).first()

		if table.player2 == 'empty':
			table.player2 = confirm['iaen']
			table.check2 = 1
			playerlist.append(table.player1)
			Rabbitmq.whointhetable(playerlist, confirm['iaen'])
			player.status =2
			db.session.commit()
			lobbyplayer = Player.query.filter_by(status=1).all()
			for a in range(len(lobbyplayer)):
				lobbylist.append(lobbyplayer[a].username)
				Rabbitmq.updatetablestillneed(lobbylist, confirm['yoney'], 2)
			return {'hevent':1}
		elif table.player3 == 'empty':
			table.player3 = confirm['iaen']
			playerlist.append(table.player1)
			playerlist.append(table.player2)
			Rabbitmq.whointhetable(playerlist, confirm['iaen'])
			table.check3 = 1
			player.status =2
			db.session.commit()
			lobbyplayer = Player.query.filter_by(status=1).all()
			for a in range(len(lobbyplayer)):
				lobbylist.append(lobbyplayer[a].username)
				Rabbitmq.updatetablestillneed(lobbylist, confirm['yoney'], 1)
			return {'hevent':1}
		elif table.player4 == 'empty':
			table.player4 = confirm['iaen']
			playerlist.append(table.player1)
			playerlist.append(table.player2)
			playerlist.append(table.player3)
			Rabbitmq.whointhetable(playerlist, confirm['iaen'])
			table.check4 = 1
			player.status =2
			table.remind1 = 13
			table.remind2 = 13
			table.remind3 = 13
			table.remind4 = 13
			table.status = 1
			db.session.commit()
			lobbyplayer = Player.query.filter_by(status=1).all()
			for a in range(len(lobbyplayer)):
				lobbylist.append(lobbyplayer[a].username)
				Rabbitmq.updatetablesdisappear(lobbylist, confirm['yoney'])
			playerlist.append(table.player4)
			Rabbitmq.dealercard(playerlist,confirm['yoney'])
			return {'hevent':1}
		else:
			return {'hevent':2}

# API 9. Game Starting
class gamestarting(restful.Resource):
	def post(self):
		playerlist = []
		cards = []
		endlist = []
		remind = 0
		confirm = request.get_json(force = True)
		player = Player.query.filter_by(username=confirm['iaen']).first()
		if confirm['eacea'] != player.password:
			return {'hevent':2}
		table = Tables.query.filter_by(titles=confirm['yoney']).first()
		cards = confirm['cards']
		remind = len(cards)
		if cards[0] == "Pass":
			remind = 0
		if confirm['iaen'] == table.player1:
			playerlist.append(table.player2)
			playerlist.append(table.player3)
			playerlist.append(table.player4)
			table.remind1 = table.remind1 - remind
			db.session.commit()
			if table.remind1 == 0:
				endlist = playerlist
				endlist.append(table.player1)
		elif confirm['iaen'] == table.player2:
			playerlist.append(table.player3)
			playerlist.append(table.player4)
			playerlist.append(table.player1)
			table.remind2 = table.remind2 - remind
			db.session.commit()
			if table.remind2 == 0:
				endlist = playerlist
				endlist.append(table.player2)
		elif confirm['iaen'] == table.player3:
			playerlist.append(table.player4)
			playerlist.append(table.player1)
			playerlist.append(table.player2)
			table.remind3 = table.remind3 - remind
			db.session.commit()
			if table.remind3 == 0:
				endlist = playerlist
				endlist.append(table.player3)
		elif confirm['iaen'] == table.player4:
			playerlist.append(table.player1)
			playerlist.append(table.player2)
			playerlist.append(table.player3)
			table.remind4 = table.remind4 - remind
			db.session.commit()
			if table.remind4 == 0:
				endlist = playerlist
				endlist.append(table.player4)
		Rabbitmq.dropcardbrocast(playerlist,confirm['iaen'],cards)
		if (table.remind1 == 0 or table.remind2 == 0 or table.remind3 == 0 or table.remind4 == 0):
			Rabbitmq.whowinthegame(endlist)
			table.status = 2
			db.session.commit()
		return {'hevent':1}


api.add_resource(createaccount, '/pinliangisgod/createaccount')
Thread(target = createaccount).start()
api.add_resource(authentication, '/pinliangisgod/aunthentication')
api.add_resource(userleavegame, '/pinliangisgod/userleavegame')
api.add_resource(createtable, '/pinliangisgod/createtable')
api.add_resource(intothetables, '/pinliangisgod/intothetables')
api.add_resource(gamestarting, '/pinliangisgod/gamestarting')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)
