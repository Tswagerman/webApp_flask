import csv
import os

from webScraper import WebScraper

def usingSettings(path):
	print('Opening file...')
	with open(path) as csvFile:  
		seen = set() #Set to keep track of duplicate rows in csv file.
		CSVdata = csv.reader(csvFile, delimiter=',') 
		for row in CSVdata:
			row = tuple(row)
			print('row = ', row, 'seen = ', seen)
			if not len(seen) == 0 and row in seen: continue #Ignoring duplicates from settings
			seen.add(row)
			desired_Price, url, receiver_email = row[0], row[1], row[2]
			webscraper = WebScraper(desired_Price, url, receiver_email)
	csvFile.close()

def checkDuplicates():
	#implement 
	pass

if __name__ == '__main__':
	#These preferences are saved in the '\data\settings.csv' file
	path = os.getcwd()
	path += '\data\settings.csv' 
	if (path): 
		usingSettings(path)	
	else:
		print('No path to settings available.')