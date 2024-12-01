import copy
from datetime import datetime
from importlib.abc import PathEntryFinder 
import re # for checking input
import random
from datetime import datetime
from PancakeQueue import PancakeQueue
from PancakeFinal import PancakeFinal
from AgentAlgorithm import SearchingAlgorithm
from ReportingUtility import ReportingUtility

class PancakeCalling():
	def __init__(self, chooice, mode='', numberOfChoice=5, printPath=False, saveToCSV=False, printVerticalReport=False):
		if (chooice == "RANDOM"):
			self.RandomInput(numberOfChoice, mode, printPath, saveToCSV, printVerticalReport)
		else :
			self.userDefine(printPath, saveToCSV, printVerticalReport)

	#START performanceTime Control
	def performanceTime(self):
		return self.Performance_Time
	#END performanceTime Control

	def stringProcess(self, inputString, printPath=False, saveToCSV=False, printVerticalReport=False):
		try :
			pancakeStack = PancakeQueue(len(inputString)-1)  
		
			algoTaken=False
			for letter in inputString:
				if(algoTaken == False):
					algorithm = letter #Choose correct algorithm function based on user input.
					algoTaken = True
				else :
					pancakeStack.push(letter)

			print("Starting Stack: ", end = "")
			print(pancakeStack)
			strPancakeStack = str(pancakeStack)
		
			if(printVerticalReport == True):
				self.Performance_Time = -10 #REPORT
			PP = PancakeFinal(int(len(inputString)-1)) 
			beforeTime = datetime.now()
			
			if algorithm == "d":
				print("Depth First Search Solution: ")
				path = PP.printPath(PP.depthFirstSearch(pancakeStack), beforeTime, printPath, saveToCSV, printVerticalReport, 'DFS', strPancakeStack) # DFS
			elif algorithm == "u":
				print("Uniform Cost Search Solution: ") 
				path = PP.printPath(PP.uniformCostSearch(pancakeStack), beforeTime, printPath, saveToCSV , printVerticalReport, 'UNIFORM', strPancakeStack) # UCS
			elif algorithm == "g":
				print("Greedy Search Solution: ") 
				path = PP.printPath(PP.greedySearch(pancakeStack), beforeTime, printPath, saveToCSV, printVerticalReport, 'GREEDY', strPancakeStack) # Greedy
			elif algorithm == "a": 
				print("A* Search Solution: ") 
				path = PP.printPath(PP.aStarSearch(pancakeStack), beforeTime, printPath, saveToCSV, printVerticalReport, 'ASTAR', strPancakeStack) # A*
					
			if(printVerticalReport == True):
				self.Performance_Time = PP.getPerformanceTime() #REPORT

			# Print Algorithm Output To Console
			self.path_counter = 0
			for i in range(len(path)):
				print(path[i])
				self.path_counter += 1
			

		except Exception as err:
			self.Performance_Time = '-1'
			print(f"Unexpected {err=}, {type(err)=}")



	def RandomInput(self, digit, mode='', printPath=False, saveToCSV=False, printVerticalReport=False):
		if (mode == ''):
			mode = ''.join((random.sample('duga', 1)))

		if (mode == "m") :
			if (digit == 5) :
				generatedNumber= ''.join((random.sample('12345', 5)))
			elif (digit == 6) :
				generatedNumber= ''.join((random.sample('123456', 6)))
			elif (digit == 7) :
				generatedNumber= ''.join((random.sample('1234567', 7)))
			elif (digit == 8) :
				generatedNumber= ''.join((random.sample('12345678', 8)))
			else:
				generatedNumber= ''.join((random.sample('1234', 4)))

			performanceTimeArray = []
			
			userIn = 'd' + generatedNumber
			print("\nSUCCESSFULLY RANDOMED INPUT WITH DEEP FIRST SEARCH : " + userIn)
			self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)
			if(printVerticalReport == True):
				performanceTimeArray.append(str(self.path_counter)) #REPORT
				performanceTimeArray.append(str(self.Performance_Time)) #REPORT
			
			userIn = 'u' + generatedNumber
			print("\nSUCCESSFULLY RANDOMED INPUT WITH UNINFORMED SEARCH : " + userIn)
			self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)
			if(printVerticalReport == True):
				performanceTimeArray.append(str(self.path_counter)) #REPORT
				performanceTimeArray.append(str(self.Performance_Time)) #REPORT
			
			userIn = 'g' + generatedNumber
			print("\nSUCCESSFULLY RANDOMED INPUT WITH GREEDY SEARCH : " + userIn)
			self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)
			if(printVerticalReport == True):
				performanceTimeArray.append(str(self.path_counter)) #REPORT
				performanceTimeArray.append(str(self.Performance_Time)) #REPORT
			
			userIn = 'a' + generatedNumber
			print("\nSUCCESSFULLY RANDOMED INPUT WITH ASTAR SEARCH : " + userIn)
			self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)
			if(printVerticalReport == True):
				performanceTimeArray.append(str(self.path_counter)) #REPORT
				performanceTimeArray.append(str(self.Performance_Time)) #REPORT

			if(printVerticalReport == True):
				performanceTimeArray.insert(0, str(userIn[1:]))
				ReportingUtility.generatePythonFile('pancakeResultVertical.csv', [performanceTimeArray], ['CASE STUDY', 'DFS STEP', 'DFS TIME', 'UNIFORMED STEP', 'UNIFORMED TIME', 'GREEDY STEP', 'GREEDY TIME', 'A* STEP', 'A* TIME'    ]) #REPORT

		else :
			if (digit == 5) :
				userIn = mode + ''.join((random.sample('12345', 5)))
			elif (digit == 6) :
				userIn = mode + ''.join((random.sample('123456', 6)))
			elif (digit == 7) :
				userIn = mode + ''.join((random.sample('1234567', 7)))
			elif (digit == 8) :
				userIn = mode + ''.join((random.sample('12345678', 8)))
			else:
				userIn = mode + ''.join((random.sample('1234', 4)))

			print("\nSUCCESSFULLY RANDOMED INPUT : " + userIn)
			self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)

	
			
	def userDefine(self, printPath=False, saveToCSV=False, printVerticalReport=False):
		# Initialize Variables + Objects
		userIn = ''

		# Start the program
		print('Welcome to Pancake Sort! Please follow the prompts below. To quit enter q at any point.')
		while(userIn != "q" and userIn !="Q"):
			print("Available Algorithms: \n")
			print("\t d - DFS \n")
			print("\t u - UCS \n")
			print("\t g - Greedy \n")
			print("\t a - A* \n")

			userIn = input("Please enter the order of pancakes followed by the desirede algorithm code e.g. d142356: ")
		
			# Take care of most input errors / ensure format is ####X
			rex = re.compile("^[a,d,g,u]{1}[1-8]{4,8}$")

			while not rex.match(userIn):
				if userIn == "q" or userIn == "Q":
					exit()
				else:
					print("Incorrect input format, please try again...")
					userIn = input("Please enter the order of pancakes (1-6) followed by the desired algorithm code, without any redudance and all number should be exists... e.g. d142356 : ")
			
			
			if (userIn != "q" and userIn !="Q"):
				if (len(userIn) != len(set(userIn))) : 
					print("Incorrect input format, please try again...")
					exit()
				else :
					self.stringProcess(userIn, printPath, saveToCSV, printVerticalReport)
					
				print() # Newline
				userIn = input("Continue? Press The Enter Key...")
				if (userIn == 'q' or userIn =='Q'):
					break

		# Empty Queue + Exit
		while not pancakeStack.isEmpty(): pancakeStack.delete()
		exit()





