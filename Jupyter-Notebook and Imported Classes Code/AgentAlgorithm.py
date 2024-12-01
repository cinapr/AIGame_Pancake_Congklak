import copy # Used for deep copy
from abc import ABCMeta, abstractmethod
import random
import time
#from func_timeout import func_timeout, FunctionTimedOut


class SearchingAlgorithm():
	#TIMEOUT_TIME = 10

	@abstractmethod
	def inputSeachingHeuristic(self,data):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass

	'''def Timeout(self, timemax, functionName, args1, args2=None, args3=None): #args=('arg1', 'arg2')
		try:
			doitReturnValue = func_timeout(timemax, functionName, args=(args1, args2, args3))
			return doitReturnValue
		except FunctionTimedOut:
			print ( "Function "+functionName+" is not completed because of timeout\n")
			pass'''

	## Search Algorithms
	# Recursive DFS, the recursion is a little messy but I believe the algorithm works
	#def depthFirstSearchCalling(self, pancakeStack, visited = None, path = None):
	#	Call = self.Timeout(self.TIMEOUT_TIME, self.depthFirstSearch, pancakeStack, visited, path)
	#	return Call

	def depthFirstSearch(self, pancakeStack, visited = None, path = None):
		# Init Variables, visited is a list of visited nodes. Path is current solution path.
		if visited == None:
			visited = []
		if path == None:
			path = []

		# If the goal has been found keep returning the path (exit recursion)
		if pancakeStack.goalFlag == 1:
			return path
		else:
			# Append Current Node To Visited and Current Path
			visited.append(pancakeStack.queue)
			path.append(pancakeStack.queue)

			# Check if current node is goal state
			if pancakeStack.goalTest() == True:
				pancakeStack.goalFlag = 1
				return path

			# Generate Fringe
			fringe = pancakeStack.generateChildrenStates()
			fringe.sort(reverse = True) # Sort fringe max -> min , this will ensure the largest child breaks the tie

			# Recursive DFS on leftmost non-visted child, prefering the largest child (to break tie)
			for i in range(3):
				if (fringe[i] not in visited):	
					#print(pancakeStack.printFlip(i, pancakeStack.getCost(i), pancakeStack.getHeuristic(i)))
					pancakeStack.queue = fringe[i]
					self.depthFirstSearch(pancakeStack, visited, path)
		
			# If all children have been visited, go up a level.
			if pancakeStack.goalFlag != 1:
				path.pop()
				pancakeStack.queue = path[-1]
				self.depthFirstSearch(pancakeStack, visited, path)
			# Exit Route For Recursion
			elif pancakeStack.goalFlag == 1:
				return path
		return

	# Non recursive UCS
	def uniformCostSearch(self, pancakeStack):
		# Init Variables
		path = []
		fringe = []
		cost = 0

		# Init fringe with start state as a multidimensional array with path and cost respectively
		fringe.append([[pancakeStack.queue], cost])

		# While the goal state has not been reached
		while pancakeStack.goalFlag != 1:
			# For every potential path on the fringe
			for i in range(len(fringe)):

				# Find the last visited node of said path
				pancakeStack.queue = fringe[i][0][-1]

				# Check if current state is goal state, if it is update path to current route
				if (pancakeStack.goalTest() == True):
					if i != 0: break # break if not the cheapest route 
					# Update path to current (cheapest) route
					path = fringe[i][0]
					pancakeStack.goalFlag = 1
					break

				# Generate the potential children of that state
				childrenStates = pancakeStack.generateChildrenStates()

				# Add children and their costs as a new pathway on the fringe
				for j in range(3):
					# Create a copy of current path and cost as new entry on the fringe
					fringe.append(copy.deepcopy([fringe[i][0], fringe[i][1]]))
				
					# Update newly created copy with child state
					fringe[-1][0].append(childrenStates[j])
					fringe[-1][1] += pancakeStack.getCost(childrenStates[j])
		
				# Delete current expanded state from fringe (only maintain currently expanding routes)
				fringe.pop(i)

			# Sort fringe by lowest cost, breaking any ties by ensuring the largest end node is first
			# After sorting the lowest costing choice will be index 0.
			fringe.sort(key = lambda x: x[0][-1], reverse = True)
			fringe.sort(key = lambda x: x[1])
		return path

	# Non Recursive Greedy Search
	def greedySearch(self, pancakeStack):
		# Init Variables
		path = []
		fringe = []
		heuristic = pancakeStack.getHeuristic()

		# Init fringe with start state as a multidimensional array with path and cost respectively
		fringe.append([[pancakeStack.queue], heuristic])

		# While the goal state has not been reached
		while pancakeStack.goalFlag != 1:
			# For every potential path on the fringe
			for i in range(len(fringe)):

				# Find the last visited node of said path
				pancakeStack.queue = fringe[i][0][-1]

				# Check if current state is goal state, if it is update path to current route
				if pancakeStack.goalTest() == True:
					if i != 0: break # break if not the cheapest route 
					# Update path to current (cheapest) route
					path = fringe[i][0]
					pancakeStack.goalFlag = 1
					break

				# Generate the potential children of that state
				childrenStates = pancakeStack.generateChildrenStates()

				# Add children and their heuristic values as a new pathway on the fringe
				for j in range(3):
					# Create a copy of current path and cost as new entry on the fringe
					fringe.append(copy.deepcopy([fringe[i][0], fringe[i][1]]))
				
					# Update newly created copy with child state
					fringe[-1][0].append(childrenStates[j])
					fringe[-1][1] =self.inputSeachingHeuristic((childrenStates[j]))
		
				# Delete current expanded state from fringe (only maintain currently expanding routes)
				fringe.pop(i)

			# Sort fringe by lowest heuristic, breaking any ties by ensuring the largest end node is first
			# After sorting the lowest heuristic choice will be index 0.
			fringe.sort(key = lambda x: x[0][-1], reverse = True)
			fringe.sort(key = lambda x: x[1])
		return path

	# Non recursive A* Search
	def aStarSearch(self,pancakeStack):
		# Init Variables
		path = []
		fringe = []
		cost = 0
		heuristic = pancakeStack.getHeuristic()

		# Init fringe with start state as a multidimensional array with path, cost, and heuristic respectively
		fringe.append([[pancakeStack.queue], cost, heuristic])
	
		# While the goal state has not been reached
		while pancakeStack.goalFlag != 1:
			# For every potential path on the fringe
			for i in range(len(fringe)):

				# Find the last visited state of said path
				pancakeStack.queue = fringe[i][0][-1]

				# Check if current state is goal state, if it is update path to current route
				if pancakeStack.goalTest() == True:
					if i != 0: break # break if not the cheapest route 
					# Update path to current (cheapest) route
					path = fringe[i][0]
					pancakeStack.goalFlag = 1
					break

				# Generate the potential children of that state
				childrenStates = pancakeStack.generateChildrenStates()

				# Add children and their costs as a new pathway on the fringe
				for j in range(3):
					# Create a copy of current path and cost as new entry on the fringe
					fringe.append(copy.deepcopy([fringe[i][0], fringe[i][1], fringe[i][2]]))
				
					# Update newly created copy with child state
					fringe[-1][0].append(childrenStates[j])
					fringe[-1][1] += pancakeStack.getCost(childrenStates[j])
					fringe[-1][2] = self.inputSeachingHeuristic(childrenStates[j])
		
				# Delete current expanded state from fringe (only maintain currently expanding routes)
				fringe.pop(i)

			# Sort fringe by lowest total cost + heuristic, breaking any ties by ensuring the largest end node is first
			# After sorting the lowest costing choice will be index 0
			fringe.sort(key = lambda x: x[0][-1], reverse = True)
			fringe.sort(key = lambda x: x[1] + int(x[2])) # Total cost + Heuristic
		return path


#import board as b
#import move as m

class competingAlgorithm():
	'''@abstractmethod
	def get_NORTH_TURN(self):
		raise NotImplementedError("Must override inputSeachingHeuristic")
	
	@abstractmethod
	def get_SOUTH_TURN(self):
		raise NotImplementedError("Must override inputSeachingHeuristic")
	
	@abstractmethod
	def get_INVALID_INDEX(self):
		raise NotImplementedError("Must override inputSeachingHeuristic")
	
	@abstractmethod
	def set_NORTH_TURN(self, NORTH_TURN1):
		raise NotImplementedError("Must override inputSeachingHeuristic")

	@abstractmethod
	def set_SOUTH_TURN(self, SOUTH_TURN1):
		raise NotImplementedError("Must override inputSeachingHeuristic")

	@abstractmethod
	def set_INVALID_INDEX(self, INVALID_INDEX1):
		raise NotImplementedError("Must override inputSeachingHeuristic")'''

	@property
	def NORTH_TURN(self):
		raise NotImplementedError

	@property
	def SOUTH_TURN(self):
		raise NotImplementedError

	@property
	def INVALID_INDEX(self):
		raise NotImplementedError

	#minMax Start
	@abstractmethod
	def shoot(self, Board,currentIndex,turn):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass

	@abstractmethod
	def move(self, First_Board,turn,index):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass

	@abstractmethod
	def nextTurn(self, turn):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass

	@abstractmethod
	def winCondition (self, Board):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass

	@abstractmethod
	def legalMove(self, Board, turn, index):
		raise NotImplementedError("Must override inputSeachingHeuristic")
		#pass
	
	@abstractmethod
	def evaluation(self,state, my_turn):
		if (my_turn==self.SOUTH_TURN):
			return state.getSouthStoreHouse()-state.getNorthStoreHouse()
		else:
			return state.getNorthStoreHouse()-state.getSouthStoreHouse()

	@abstractmethod
	def maximum(self, state, depth, my_turn, alpha, beta, is_prune):
		if my_turn == self.SOUTH_TURN:
			init = 0
		else:
			init = 8
		max_value = -999
		for i in range (init, init+7):
			if state.board[i] != 0:
				new_state, next_turn = self.move(self, state, my_turn, i)
				score = self.minimax(self, new_state, next_turn, depth-1, my_turn, alpha, beta, my_turn)
				max_value = max(max_value, score)
				alpha = max(alpha, score)
				if is_prune and beta <= alpha:
					break
		return max_value
		
	@abstractmethod
	def minimum(self, state, depth, my_turn, alpha, beta, is_prune):
		if self.nextTurn(self, my_turn) == self.SOUTH_TURN:
			init = 0
		else:
			init = 8

		min_value = 999
		for i in range (init, init+7):
			if state.board[i] != 0:
				new_state, next_turn =  self.move(self, state, self.nextTurn(self, my_turn), i)
				score = self.minimax(self,new_state, next_turn, depth-1, my_turn, alpha, beta, self.nextTurn(self, my_turn))
				min_value = min(min_value, score)
				beta = min(beta, min_value)
				if is_prune and beta <= alpha:
					break
		return min_value
		
	@abstractmethod
	def minimax(self, state, current_turn, depth, my_turn, alpha, beta, parent_turn):
		if depth == 0:
			return self.evaluation(self, state, current_turn)

		if (current_turn==my_turn):
			return self.maximum(self, state, depth, my_turn, alpha, beta, parent_turn != current_turn)
		else:
			return self.minimum(self, state, depth, my_turn, alpha, beta, parent_turn != current_turn)

	@abstractmethod
	def best_move (self, state, turn, depth):
		idx = 0
		if (turn == self.NORTH_TURN):
			if (state.checkAllNorthHouseEmpty()):
				idx = self.INVALID_INDEX
		else:
			if (state.checkAllSouthHouseEmpty()):
				idx = self.INVALID_INDEX
		if idx == self.INVALID_INDEX:
			return idx

		max_value = -9999
		if turn == self.SOUTH_TURN:
			init = 0
		else:
			init = 8
		for i in range (init, init+7):
			if state.board[i] != 0:
				next_state, next_turn = self.move(self, state, turn, i)
				value = self.minimax(self, next_state, next_turn, depth-1, turn, -999, 999, turn)
				if max_value <= value:
					max_value = value
					idx = i
		return idx


#minMax End


	




