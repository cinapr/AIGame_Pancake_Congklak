#from bdb import checkfuncname
import os
import csv

class ReportingUtility():
	def __init__():
		pass

	def generatePythonFile(filePath, data, header=['ALGORITHM NAME', 'CASE/WINNER', 'TIME', 'PERFORMANCE'], myDelimiter=';'):
		'''
		#EXAMPLE
		student_header = ['name', 'age', 'major', 'minor']
		student_data = [
			['Jack', 23, 'Physics', 'Chemistry'],
			['Sophie', 22, 'Physics', 'Computer Science'],
			['John', 24, 'Mathematics', 'Physics'],
			['Jane', 30, 'Chemistry', 'Physics']
		]
		'''

		if(ReportingUtility.checkFileExist(filePath) == False):
			with open(filePath, 'w', encoding="UTF8") as file_: #1.create new file
				writer = csv.writer(file_,delimiter=myDelimiter) # 2. Create a CSV writer
				
				if(header != []):
					writer.writerow(header) # 3. Write header to file

				writer.writerows(data)

				file_.close()


		else:
			with open(filePath, mode='a', encoding="UTF8") as file_: #1.open old file
				writer = csv.writer(file_,delimiter=myDelimiter) # 2. Create a CSV writer
				writer.writerows(data) #filldata
				file_.close()

		 
			

	def checkFileExist(pathFile = './statistic.csv'):
		return os.path.isfile(pathFile)

	def checkFolderExist(pathFolder = './final_data_folder'):
		return os.path.isdir(pathFolder)

	def checkPathExist(path = './final_data_folder'):
		return os.path.exists(path)







