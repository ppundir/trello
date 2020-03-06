import uuid
class Card:
	def __init__(self,name,description=None,user=None):
		self.id = str(uuid.uuid4())
		self.name = name
		self.description = description
		self.user = user

	def getId(self):
		return self.id

	def setId(self,id):
		self.id = id

	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

	def getDescription(self):
		return self.description

	def setDescription(self,description):
		self.description = description

	def setUser(self,user):
		self.user = user

	def getUser(self):
		return self.user

	def removeUser(self):
		self.user = None

	def delete(self):
		del self

	