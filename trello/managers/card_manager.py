class CardManager:
	def show(self,card):
		output = {}
		output["id"] = card.getId()
		output["name"] = card.getName()
		output["description"] = card.getDescription()
		output["user"] = card.getUser().getName()		
		return output