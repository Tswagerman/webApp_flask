import csv
import os

import SQL
from webScraper import WebScraper

def usingSettings(path):
	print('Opening file...')
	c = SQL.select_distinct_data()
	for row in c:
		desired_Price, url, receiver_email = row[0], row[1], row[2]
		webscraper = WebScraper(desired_Price, url, receiver_email)

if __name__ == '__main__':
	#These preferences are saved in the '\data\settings.csv' file
	path = os.getcwd()
	path += '\data\settings.csv' 
	if (path): 
		usingSettings(path)	
	else:
		print('No path to settings available.')