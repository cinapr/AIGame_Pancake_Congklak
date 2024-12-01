from CongklakBoard import CongklakBoard #as b
from CongklakMove import CongklakMove #as m
import random

class CongklakRandomBot():
	def random_move(board, turn):
		m = CongklakMove()
		board = CongklakBoard()
		#idx = m.INVALID_INDEX
		idx = m.get_INVALID_INDEX()
		if (turn == m.get_NORTH_TURN()):
			if (not board.checkAllNorthHouseEmpty()):
				idx = random.randint(8,15)
				while (not m.legalMove(board, turn, idx)):
					idx = random.randint(8,15)
		else:
			if (not board.checkAllSouthHouseEmpty()):
				idx = random.randint(0,7)
				while (not m.legalMove(board, turn, idx)):
					idx = random.randint(0,7)
		return idx


	
