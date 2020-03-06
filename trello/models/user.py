import uuid
class User:
	def __init__(self,name,email):
		self.id = str(uuid.uuid4())
		self.name = name
		self.email = email

	def __repr__(self):
		return self.id

	def getId(self):
		return self.id

	def setId(self,id):
		self.id = id

	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

	def getEmail(self):
		return self.email

	def setEmail(self,email):
		self.email = email

