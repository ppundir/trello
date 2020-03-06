import uuid
class List:
	def __init__(self,name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.cards = []

	def getId(self):
		return self.id

	def setId(self,id):
		self.id = id

	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

	def getCards(self):
		return self.cards

	def addCard(self,card):
		self.cards.append(card)

	def removeCard(self,card):
		self.cards.remove(card)

	def delete(self):
		for card in self.cards:
			card.delete()
		del self