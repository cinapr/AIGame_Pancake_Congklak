#from types import _StaticFunctionType
import CongklakBoard as b
import copy
from AgentAlgorithm import competingAlgorithm

class CongklakMove(competingAlgorithm):
	
	NORTH_TURN = 1 #atas
	SOUTH_TURN = 0 #bawah
	INVALID_INDEX = -1

	def __init__(self):
		#self.NORTH_TURN = 1 #atas
		#self.SOUTH_TURN = 0 #bawah
		#self.INVALID_INDEX = -1
		pass

	def get_INVALID_INDEX(self):
		return self.INVALID_INDEX

	def get_SOUTH_TURN(self):
		return self.SOUTH_TURN

	def get_NORTH_TURN(self):
		return self.NORTH_TURN

	#Tembak shell
	def shoot(self, Board,currentIndex,turn):
		point = Board.getShell(Board.getOpponentIndex(currentIndex)) +  Board.getShell(currentIndex)
		if(turn == self.NORTH_TURN):
			Board.addShell(b.NORTH_STOREHOUSE,point)
		else: #turn == SOUTH_TURN
			Board.addShell(b.SOUTH_STOREHOUSE,point)
		# print(Board.printBoard())

	#Mengembalikan state board setelah move dan giliran siapa setelah move dieksekusi
	def move(self, First_Board,turn,index):
		Board = copy.deepcopy(First_Board)
		if(self.legalMove(self, Board,turn,index)):
			loop = False
			currentIndex = index
			if(turn == self.SOUTH_TURN):
				remainingStep = Board.getShell(index)
				while(remainingStep > 0):
					currentIndex = currentIndex + 1
					if(currentIndex == 15):
						loop = True
						currentIndex = 0

				
					if(remainingStep == 1 and Board.isEmptyHouse(currentIndex) and not(Board.isSouthStoreHouse(currentIndex))):
						if(loop and Board.southSite(currentIndex) and not(Board.isEmptyHouse(Board.getOpponentIndex(currentIndex)))):
							Board.addShell(currentIndex,1)
							self.shoot(self, Board,currentIndex,turn)
						else:
							Board.addShell(currentIndex,1)
					elif(remainingStep == 1 and not(Board.isSouthStoreHouse(currentIndex))):
						Board.addShell(currentIndex,1)
						remainingStep = remainingStep + Board.getShell(currentIndex)
					else: 
						Board.addShell(currentIndex,1)

					remainingStep = remainingStep - 1

				if(currentIndex != b.SOUTH_STOREHOUSE):
					turn = self.NORTH_TURN

			else: #(turn == NORTH_TURN)
				remainingStep = Board.getShell(index)
				while(remainingStep > 0):
					currentIndex = currentIndex + 1

					if(currentIndex ==16):
						currentIndex = 0

					if(currentIndex == 7):
						loop = True
						currentIndex = 8

				
					if(remainingStep == 1 and Board.isEmptyHouse(currentIndex) and not(Board.isNorthStoreHouse(currentIndex))):
						if(loop and Board.northSite(currentIndex) and not(Board.isEmptyHouse(Board.getOpponentIndex(currentIndex)))):
							Board.addShell(currentIndex,1)
							self.shoot(self, Board,currentIndex,turn)
						else:
							Board.addShell(currentIndex,1)
					elif(remainingStep == 1 and not(Board.isNorthStoreHouse(currentIndex))):
						Board.addShell(currentIndex,1)
						remainingStep = remainingStep + Board.getShell(currentIndex)
					else: 
						Board.addShell(currentIndex,1)

					remainingStep = remainingStep - 1

				if(currentIndex != b.NORTH_STOREHOUSE):
					turn = self.SOUTH_TURN

			return Board,turn
		else:
			return Board, self.nextTurn(self, turn)


	def nextTurn(self, turn):
		if turn == self.SOUTH_TURN:
			return self.NORTH_TURN
		else:
			return self.SOUTH_TURN

	#Kondisi menang
	def winCondition (Board):
		if(Board.checkAllHouseEmpty()):
			return Board.getSouthStoreHouse() > Board.getNorthStoreHouse()

	#Legal move untuk South maupun north
	def legalMove(self, Board, turn, index):
		if index == self.INVALID_INDEX:
			return False
		
		if(turn == self.NORTH_TURN):
			return not(Board.checkAllNorthHouseEmpty()) and not(Board.isEmptyHouse(index)) and Board.northSite(index)
  
		else:#(turn == SOUTH_TURN)
			return not(Board.checkAllSouthHouseEmpty()) and not(Board.isEmptyHouse(index)) and Board.southSite(index)

	
	# state = b.Board()
	# move(state,SOUTH_TURN, 0)
	# state.printBoard()



