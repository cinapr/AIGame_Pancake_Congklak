from CongklakCMD import MyCongklakCMD

class CongklakApp():
	def __init__(self, _mode, difficulity, first_turn, RandomFirstMove, saveToCSV=False):
		congklak = MyCongklakCMD(_mode, difficulity, first_turn, RandomFirstMove, saveToCSV)
