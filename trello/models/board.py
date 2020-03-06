import uuid
from trello.config.settings import BASE_URL
from trello.models.privacy import Privacy

class Board(object):
	def __init__(self,name,privacy=Privacy.PUBLIC):
		self.id = str(uuid.uuid4())
		self.name = name
		self.privacy = privacy
		self.url = BASE_URL + '/board/' + self.id
		self.members = []
		self.lists = []
		print ("Created board: " + self.id)

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

	def getPrivacy(self):		
		return self.privacy.name

	def setPrivacy(self,privacy):
		self.privacy = privacy

	def getUrl(self):
		return self.url

	def setUrl(self,url):
		self.url = url

	def getMembers(self):
		return self.members

	def addMember(self,member):
		self.members.append(member)

	def removeMember(self,member):
		self.members.remove(member)

	def getLists(self):
		return self.lists

	def addList(self,listobj):
		self.lists.append(listobj)

	def removeList(self,listobj):
		self.lists.remove(listobj)

	def delete(self):
		for listobj in self.lists:
			listobj.delete()
		del self



