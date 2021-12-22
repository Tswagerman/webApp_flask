import requests
import csv
import re
import datetime 
import smtplib, ssl #sendNotification
import os
from os import path

from bs4 import BeautifulSoup, SoupStrainer

class WebScraper:
	def __init__(self, desired_price, url, receiver_email):
		self.current_Price = 0
		self.desired_Price = int(desired_price) #Important that this is interpreted as int, when comparing to current price
		self.url = url
		self.receiver_email = receiver_email
		self.control()
		#url = "https://www.pricerunner.dk/pl/126-5049980/Analoge-kameraer/Fujifilm-Instax-Mini-Film-20-pack-Sammenlign-Priser"

	def control(self):
		print('SCRAPY IS ON IT!')
		self.extractCurrentPrice()
		if self.current_Price <= self.desired_Price:
			try:
				SUBJECT = "Scrapy's shiny!"
				message = """Subject: %s\n\n""" % (SUBJECT) + f"ALERT ALERT, BUY YOUR SHINY STUFF. IT IS CHEAP!! \nCurrent Price: {self.current_Price} \nDesired Price: {self.desired_Price} \nItem: {self.url}"
				self.sendNotification(message)
				print('sent notification')
			except:
				print('failed to send notification')
		self.saveHistory()
		
	def extractCurrentPrice(self):
		page = requests.get(self.url) 
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		#'currency':'DKK', old attr that used to work for scraping the lowest price
		#First class found is the minimal price. The lowest price is the first item found on the website with the corresponding attributes
		data = soup.find('span', attrs={'class':'SnarOLmYcb Ci0mGVkzmW Fg7gKEY8SV eSiwcTiHBc css-d5txxz'})
		print('data = ', data)
		self.current_Price = data.text.strip() 
		self.current_Price = re.sub(r'[aA-zZ]+', '', self.current_Price, re.I) 
		self.current_Price = int(self.current_Price.replace(".", ""))	
	
	def sendNotification(self, message):
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "notifications.pricerunner.scrapy@gmail.com" 
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			self.login(sender_email, server)
			server.sendmail(sender_email, self.receiver_email, message)

	def saveHistory(self):
		mydate = datetime.datetime.now().strftime('%d %b %Y - %H:%M')	#add date, so history is build up.
		csvdata = 'Price = ' + str(self.current_Price) + ', Date = ' + str(mydate)
		cwd = os.getcwd() #current working directory
		savePath = cwd + "\data\history.csv"
		with open(savePath, 'a', newline='\n') as file:
			mywriter = csv.writer(file, delimiter=',')
			mywriter.writerow([csvdata]) #the [] are there to make sure the entire string is saved as one.

	def login(self, sender_email, server):
		password = 'pricerunner' 
		try:
			server.login(sender_email, password)
		except:
			print('except')
			#Send error message or smth
			#?self.login(sender_email, server)