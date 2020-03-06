import sys
sys.path.insert(0,'/Users/spoylios/Desktop/mc')
from trello.models.board import Board
from trello.models.user import User
from trello.models.card import Card
from trello.models.list import List
from trello.managers.board_manager import BoardManager
from trello.managers.list_manager import ListManager
from trello.models.privacy import Privacy
#SHOW
#BOARD CREATE work@tech
print ("BOARD CREATE")
board= Board("recommendation_v1")
board_output = BoardManager().show(board)
print (board_output)

print ("#######")
print ("#change name and privacy")
board.setPrivacy(Privacy.PRIVATE)
board.setName("recommendation_v2")
board_output = BoardManager().show(board)
print (board_output)

print ("#######")
print ("add memeber 1 and 2")

member1 = User('Pawan','hitechpundir@yahoo.com')
print (member1)

member2 = User('Raj','raj34@gmail.com')
print (member2)
board.addMember(member1)
board.addMember(member2)
board_output = BoardManager().show(board)
print (board_output)

print ("#######")
print ("remove member 1")
board.removeMember(member1)	
board_output = BoardManager().show(board)
print (board_output)
print ("#####")

print ("List Create")
listobj1 = List('MigrationProject')
list_output = ListManager().show(listobj1)
print (list_output)

print ("#####")
print ("List Create")
listobj2 = List('Testing')
list_output = ListManager().show(listobj2)
print (list_output)
print ("#####")
print ("add lists to board")
board.addList(listobj1)
board.addList(listobj2)
board_output = BoardManager().show(board)
print (board_output)
print ("#####")

print ("assign and create cards")
card1 = Card('migrate data','full historical data in batches',member1)
card2 = Card('train model','model training and tetsing',member2)


listobj1.addCard(card1)
listobj1.addCard(card2)


card3 = Card('test automation','full test cases',member1)
listobj2.addCard(card3)

board_output = BoardManager().show(board)
print (board_output)
print ("#####")

#board.delete()
#print (board)




