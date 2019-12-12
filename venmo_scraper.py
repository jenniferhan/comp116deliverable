# Python Script to access the Venmo API and save each transaction into an SQLite database

import requests
import json
import time
import sqlite3

while 1:
	i = 0
	while i < 19:

		conn = sqlite3.connect('venmo_new.db')
		c = conn.cursor()
		c.execute('CREATE TABLE IF NOT EXISTS venmo_data(actor_name TEXT, target_name TEXT, paymentOrCharge TEXT, message TEXT, actorPicture TEXT, targetPicture TEXT)')
		response = requests.get("https://venmo.com/api/v5/public")
		data = json.loads(response.text)

		actor = data['data'][i]['actor']['username']
		target = data['data'][i]['transactions'][0]['target']['username']
		actorPicture = data['data'][i]['actor']['picture']
		targetPicture = data['data'][i]['transactions'][0]['target']['picture']
		message = data['data'][i]['message']
		if (data['data'][i]['type'] == 'payment'):
			paymentOrCharge = 'payment'
		elif (data['data'][i]['type'] == 'charge'):
			paymentOrCharge = 'charge'

		c.execute("INSERT INTO venmo_data (actor_name, target_name, paymentOrCharge, message, actorPicture, targetPicture) VALUES (?, ?, ?, ?, ?, ?)", (actor, target, paymentOrCharge, message, actorPicture, targetPicture))
		i+=1
		conn.commit()
		print("Transaction has been committed.")

	time.sleep(1000)

