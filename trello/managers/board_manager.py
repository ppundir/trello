from trello.managers.list_manager import ListManager
class BoardManager:
	def show(self,board):
		output = {}
		output["id"] = board.getId()
		output["name"] = board.getName()
		output["privacy"] = board.getPrivacy()
		output["members"] = []
		for member in board.getMembers():
			output["members"].append({"name":member.getName(),"email":member.getEmail()})

		output["lists"] = []
		for listobj in board.getLists():
			output["lists"].append(ListManager().show(listobj))		
			
			
		return output