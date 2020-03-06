from trello.managers.card_manager import CardManager
class ListManager:
	def show(self,listobj):
		output = {}
		output["id"] = listobj.getId()
		output["name"] = listobj.getName()
		
		output["cards"] = []
		for card in listobj.getCards():
			output["card"].append(CardManager().show(card))
			
		return output