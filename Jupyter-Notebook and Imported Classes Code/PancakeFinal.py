import copy # Used for deep copy
import re # for checking input
from datetime import datetime 
from PancakeQueue import PancakeQueue
from AgentAlgorithm import SearchingAlgorithm
from ReportingUtility import ReportingUtility

class PancakeFinal(SearchingAlgorithm):
	## Helper Functions
	# Prints all of the flips, cost, and heuristic values of a specific path taken to get to a goal state

	def __init__(self,queueAmount): 
		self.queueAmount = queueAmount
		self.performanceTime = -1

	def getPerformanceTime(self):
		return self.performanceTime
		
	def inputSeachingHeuristic(self,data):
		for pos in range(0, self.queueAmount-1):
			if (data[pos] != str(self.queueAmount-pos)):
				return str(self.queueAmount-pos)
			return "0"

	def printPath(self, path, beforeTime, printPath=False, saveToCSV=False, printVerticalReport = False, AlgorithmName='', TestingCase=''):
		# Get length of path
		n = len(path)
		output = []
		cost = 0

		# Build Output For Each Flip
		if(printPath == True or printVerticalReport == True) : 
			for i in range(n - 1):
				# Reinit Variables
				builder = ""
				flipFlag = 0
				heuristic = "0"
				currCost = 0

				# Build string representation of flip eg "12|24 g=3, h=0"
				for j in range(self.queueAmount):
					if (path[i][j] != path[i+1][j] and flipFlag != 1):
						flipFlag = 1
						currCost += (self.queueAmount - j)
						builder += "|"
					builder += path[i][j]
				
				heuristic = "0"
				for pos in range(0, self.queueAmount-1):
					if (path[i][pos] != str(self.queueAmount-pos)):
						heuristic = str(self.queueAmount-pos)
						break
	
				builder += (" g=" + str(cost) + ", " + "h=" + heuristic)
				cost += currCost
				output.append(builder)
	
		# Goal State (final append)
		builder = "Final State: "
		self.path_counter = 0
		for i in range(self.queueAmount):
			builder += path[n-1][i]
			self.path_counter += 1

		afterTime = datetime.now()
		self.performanceTime = str((afterTime - beforeTime).total_seconds())

		builder += (" g=" + str(cost) + ", " + "h=" + str(0))
		builder += "\n"
		builder += ("Time : " + str(self.performanceTime))
		output.append(builder)

		if(saveToCSV == True):
			ReportingUtility.generatePythonFile('pancakeResult.csv', [[AlgorithmName, TestingCase, self.performanceTime, " g=" + str(cost) + ", " + "h=" + str(0)]])

		return output


	