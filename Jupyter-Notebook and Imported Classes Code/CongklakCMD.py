from asyncio.windows_events import NULL
import sys, os
from xmlrpc.client import DateTime
from datetime import datetime
#import CongklakBoard as b
#import CongklakMove as m
from CongklakBoard import CongklakBoard as b
from CongklakMove import CongklakMove as m
from CongklakRandomBot import CongklakRandomBot #as randombot
from AgentAlgorithm import competingAlgorithm #as minimax
from ReportingUtility import ReportingUtility

DELAY_TIME = 0.005

class MyCongklakCMD():
	global DELAY_TIME
	Board = b()
	Mode = ""
	Turn = m.SOUTH_TURN
	Difficulty = 2
	startTime = datetime.now()

	def __init__(self, _mode, difficulity, first_turn, RandomFirstMove, saveToCSV=False):
		self.minimax = competingAlgorithm()
		self.randombot = CongklakRandomBot()
		if (_mode != "MvM"):
			RandomFirstMove = False #RandomFirstMove only works for Minimax vs Minimax
		self.startCMD(_mode, difficulity, first_turn, RandomFirstMove, saveToCSV)

	def startCMD(self, mode, difficulity, first_turn, RandomFirstMove, saveToCSV=False):
		self.Mode = mode #MvR
		self.difficulty = difficulity #1hard, 6easy
		self.saveToCSV = saveToCSV
		self.Turn = first_turn #MINMAX SOUTH, RANDOM NORTH
		self.RandomFirstMove = RandomFirstMove
		self.set_first_turn(first_turn)

	def setWinner(self, winner, performanceTime):
		self.Winner = winner
		self.performanceTime = performanceTime
		

	def set_info_lbl(self):
		_text = ""

		if (self.Mode == "MvP"):
			_text = "Bot Minimax vs Player"
		elif (self.Mode == "RvP"):
			_text = "Bot Random vs Player"
		elif (self.Mode == "MvM"):
			_text = "Bot Minimax vs Bot Minimax"
		else: #self.Mode=="MvR"
			_text = "Bot Minimax vs Bot Random"
		self.boardLay.gamemodeLbl.text = _text
		print(_text)

		player1 = ""
		player2 = ""

		if ((self.Mode == "MvP") or (self.Mode == "RvP")):
			player1 = "Player"
			player2 = "Bot"
		elif (self.Mode == "MvM") :
			player1 = "Minimax Bot"
			player2 = "Minimax Bot"
		else:
			player1 = "Minimax Bot"
			player2 = "Random Bot"

		print(player1)
		print(player2)

	def set_turn_lbl(self, _turn):
		_text = ""

		if (_turn == m.SOUTH_TURN):
			if (self.Mode == 'MvP' or self.Mode == 'RvP'):
				_text = "Player"
			elif (self.Mode == 'MvM'):
				_text = "Bot MinMax 2"
			else:
				_text = "Bot Minimax"
		else: #NORTH_TURN
			if (self.Mode == 'MvP' or self.Mode == 'RvP'):
				_text = "Bot"
			elif (self.Mode == 'MvM'):
				_text = "Bot MinMax 1"
			else:
				_text = "Bot Random"

		print(_text +  " Turn")

	def set_first_turn(self, _turn):
		self.Turn = _turn
		#self.boardLay.remove_widget(self.boardLay.turnLay)
		self.set_turn_lbl(_turn)
		self.initiate_play()

	def initiate_play(self):
		self.startTime = datetime.now()
		self.first_turn_M1 = 0
		self.first_turn_M2 = 0

		print(self.Mode + " " + str(self.Turn))
		if ((self.Mode == "MvP" or self.Mode == "RvP") and self.Turn == m.NORTH_TURN):
			self.player_2_move(DELAY_TIME)
		elif (self.Mode == "MvR" and self.Turn == m.SOUTH_TURN):
			self.player_1_bot_move(DELAY_TIME)
		elif (self.Mode == "MvR" and self.Turn == m.NORTH_TURN):
			self.player_2_move(DELAY_TIME)
		elif (self.Mode == "MvM" and self.Turn == m.SOUTH_TURN):
			self.player_1_bot_move(DELAY_TIME)
		elif (self.Mode == "MvM" and self.Turn == m.NORTH_TURN):
			self.player_2_move(DELAY_TIME)
		else :
			print(self.Mode + " " + str(self.Turn))

	def player_1_move(self, hole_id):
		if (self.Board.checkAllHouseEmpty()):
			self.add_win_lay()

		if (self.Board.checkAllSouthHouseEmpty()):
			self.Turn = m.NORTH_TURN
			self.player_2_move(DELAY_TIME)
		else:
			if ((self.Mode == "MvP" or self.Mode == "RvP") and self.Turn == m.SOUTH_TURN and self.Board.board[hole_id]!=0 ): #player move
				if (hole_id < 7):
					self.Board, self.Turn = m.move(self.Board, m.SOUTH_TURN, hole_id)
			
			print(str(datetime.now()) + "Player 1 move: " + str(hole_id))
			self.set_turn_lbl(self.Turn)
			self.draw_board()

			if (self.Board.checkAllHouseEmpty()):
				self.add_win_lay()
			else:
				if (self.Turn != m.SOUTH_TURN):
					self.player_2_move(DELAY_TIME)
				elif (self.Board.checkAllSouthHouseEmpty()):
					self.Turn = m.NORTH_TURN
					self.player_2_move(DELAY_TIME)
				else:
					print("ELSE Q")
	
	def player_1_bot_move(self, dt):
		if (self.Board.checkAllHouseEmpty()):
			self.add_win_lay()

		if (self.Board.checkAllSouthHouseEmpty()):
			self.Turn = m.NORTH_TURN
			self.player_2_move(DELAY_TIME)
		else:
			if ((self.Mode == "MvR") | (self.Mode == "MvM")): #minimax bot
				if (self.Mode == "MvM" and self.first_turn_M1 <= 3 and self.RandomFirstMove == True): #random bot
					#bot_move = self.randombot.random_move(self.Board, self.Turn) #CEK ULANG INI
					bot_move = self.randombot.random_move(self.Turn)
					self.first_turn_M1 += 1
				else:
					#bot_move = self.minimax.best_move(self.Board, self.Turn, self.Difficulty)
					bot_move = m.best_move(m, self.Board, self.Turn, self.Difficulty) #TESTHERE
				self.Board, self.Turn = m.move(m, self.Board, m.SOUTH_TURN, bot_move)
				print(str(datetime.now()) + "Player 1 move: " + str(bot_move))

				self.set_turn_lbl(self.Turn)


				if (self.Board.checkAllHouseEmpty()):
					self.add_win_lay()
				else:
					if (self.Turn != m.SOUTH_TURN):
						self.player_2_move(DELAY_TIME)
					else:
						self.player_1_bot_move(DELAY_TIME)
			else:
				print("ELSE P")

	def player_2_move(self, dt):
		if (self.Board.checkAllHouseEmpty()):
			self.add_win_lay()

		if (self.Board.checkAllNorthHouseEmpty()):
			self.Turn = m.SOUTH_TURN
			if ((self.Mode == "MvR") or (self.Mode == "MvM")):
				self.player_1_bot_move(DELAY_TIME)
			else:
				print("ELSE M")
		else:
			if (self.Mode == "RvP" or self.Mode == "MvR" or (self.Mode == "MvM" and self.first_turn_M2 <= 3 and self.RandomFirstMove == True)): #random bot
				#bot_move = self.randombot.random_move(self.Board, self.Turn) #CEK ULANG INI
				bot_move = self.randombot.random_move(self.Turn)
				self.first_turn_M2 += 1
			else: #minimax bot
				bot_move = m.best_move(m, self.Board, self.Turn, self.Difficulty)
				#bot_move = self.minimax.best_move(self.Board, self.Turn, self.Difficulty)

			print(str(datetime.now()) + "Player 2 move: " + str(bot_move))
			self.Board, self.Turn = m.move(m, self.Board, m.NORTH_TURN, bot_move)
			self.set_turn_lbl(self.Turn)

			if (self.Board.checkAllHouseEmpty()):
				self.add_win_lay()
			else:
				if (self.Turn == m.NORTH_TURN):
					self.player_2_move(DELAY_TIME)
				elif ((self.Mode == "MvR") | (self.Mode == "MvM")):
					self.player_1_bot_move(DELAY_TIME)
				elif ((self.Mode == "MvP" or self.Mode == "RvP") and self.Board.checkAllSouthHouseEmpty()):
					self.Turn = m.NORTH_TURN
					self.player_2_move(DELAY_TIME)
				else:
					print("ELSE Z" + str(self.Mode) + str(self.Board.checkAllSouthHouseEmpty()) + str(self.Turn))

	def add_win_lay(self):
		self.endTime = datetime.now()

		if (self.Mode == "MvP" or self.Mode == "RvP"):
			_south = "Player"
			if (self.Mode == "MvP"):
				_north = "Minimax Bot"
			else:
				_north = "Random Bot"
		elif (self.Mode == "MvM") :
			_south = "Minimax Bot 2"
			_north = "Minimax Bot 1"
		else: #Minimax vs Random
			_south = "Minimax Bot"
			_north = "Random Bot"

		winnerName = ''
		#if (self.minimax.evaluation(self.Board, m.SOUTH_TURN) > 0):
		if (m.evaluation(m,self.Board, m.SOUTH_TURN) > 0):
			_text = _south + " WINS"
			winnerName = _south
		#elif (self.minimax.evaluation(self.Board, m.SOUTH_TURN) < 0):
		elif (m.evaluation(m,self.Board, m.SOUTH_TURN) < 0):
			_text = _north + " WINS"
			winnerName = _north
		else:
			_text = "IT'S A TIE"
			winnerName = 'TIE'
		
		TimeDiff = (self.endTime - self.startTime).total_seconds()
		print(_text + " IN : " + str(TimeDiff) + " SECONDS")

		self.setWinner(winnerName,str(TimeDiff))

		if (self.saveToCSV == True):
			ReportingUtility.generatePythonFile('congklakResult.csv', [[self.Mode, winnerName, str(TimeDiff), '']]) #REPORT
	
	def set_difficulty(self, depth):
		self.Difficulty = depth

