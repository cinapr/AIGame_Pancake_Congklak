import copy # Used for deep copy
import re # for checking input

## Queue Structure (Stack of Pancakes and functions)
class PancakeQueue(object):
	def __init__(self, queueAmount = 6): 
		self.queueAmount = queueAmount
		self.queue = []
		self.goalFlag = 0 # Used to escape recursion in DFS
  
	def __str__(self): 
		return ' '.join([str(i) for i in self.queue]) 
  
	# for checking if the queue is empty 
	def isEmpty(self): 
		return len(self.queue) == [] 
  
	# for inserting an element in the queue 
	def push(self, data): 
		self.queue.append(data)

	# for deleting an element based on Priority 
	def delete(self): 
		try: 
			max = 0
			for i in range(len(self.queue)): 
				if self.queue[i] > self.queue[max]: 
					max = i 
			item = self.queue[max] 
			del self.queue[max] 
			return item 
		except IndexError: 
			print() 
			exit()
	
	# Returns the cost of flipping from one state to the next
	def getCost(self, nextState):
		for i in range(self.queueAmount):
			if self.queue[i] != nextState[i]:
				return (self.queueAmount - i)
		return 0
				
	# Returns the heuristic of a pancake
	def getHeuristic(self):
		'''if self.queue[0] != "4":
			return "4"
		if self.queue[1] != "3":
			return "3"
		if self.queue[2] != "2":
			return "2"
		if self.queue[3] != "1":
			return "1"
		return "0"'''

		for pos in range(0, self.queueAmount-1):
			if self.queue[pos] != str(self.queueAmount-pos):
				return str(self.queueAmount-pos)
		return "0"
	
	# Checks if the current state is a goal state
	def goalTest(self):
		'''if (self.queue[0] == "4" and self.queue[1] == "3" and self.queue[2] == "2" and self.queue[3] == "1"): 
			return True
		return False'''
		for pos in range(0, self.queueAmount-1):
			if (self.queue[pos] != str(self.queueAmount-pos)):
				return False
		return True

	# Flip pancake stack from specific point
	def flip(self, data):
		# Variables and Objects
		snapshot = self.queue[:] # Shallow copy so queue isn't modified.
		tempQueue = [] # Temporary queue for rebuilding the stack	
		pancake = self.queue[data] # Set marker for the value at position [data]

		# Pop all pancakes to the right of the pancake at position [data] then pop that pancake too
		while pancake in snapshot:
			tempQueue.append(snapshot.pop())

		# Rebuild queue (flipped from position [data])
		for pancake in tempQueue:
			snapshot.append(pancake)
		
		# Return flipped stack
		return snapshot

	# Helper function, returns formatted output (visualization) for what flip just took place and for what costs
	def printFlip(self,data,cost,heuristic):
		builder = ''
		for i in range(self.queueAmount-1):
			if i == data:
				builder += "|"
			builder += self.queue[i]
		builder += (" g=" + str(cost) + ", " + "h=" + str(heuristic))
		return builder

	# Takes the current state and lists the potential next states
	def generateChildrenStates(self):
		stateA = self.flip(0)
		stateB = self.flip(1)
		stateC = self.flip(2)
		return [stateA, stateB, stateC]