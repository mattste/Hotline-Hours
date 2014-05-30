import httplib2
import os
import gflags
import sys
import json

from apiclient.discovery import build
from oauth2client import client 
from oauth2client.file import Storage
from oauth2client import tools



class Configure(object): 
	'''
	# Configure Google Calendar API credentials, create a new object to interact
	# with the API
	'''
	FLAGS = gflags.FLAGS

	def __init__(self):
		pass

	# Set up a Flow object to be used if we need to authenticate. This
	# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
	# the information it needs to authenticate. Note that it is called
	# the Web Server Flow, but it can also handle the flow for native
	# applications
	# The client_id and client_secret can be found in Google Developers Console
	
	def setup(self):
	
		# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
		# application, including client_id and client_secret. You can see the Client ID
		# and Client secret on the APIs page in the Cloud Console:
		# <https://cloud.google.com/console#/project/102389784529/apiui>
		# CLIENT_SECRETS = os.path.join(os.path.basename(__file__), 'client_secrets.json')
		CLIENT_SECRETS = 'client_secrets.json'
		FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
		  scope=[
		      'https://www.googleapis.com/auth/calendar',
		      'https://www.googleapis.com/auth/calendar.readonly',
		    ],
		    message=tools.message_if_missing(CLIENT_SECRETS))
		

		# If the Credentials don't exist or are invalid, run through the native client
		# flow. The Storage object will ensure that if successful the good
		# Credentials will get written back to a file.
		storage = Storage('calendar.dat')
		self.credentials = storage.get()
		try:
			api_keys_file = open('google_secrets.json')
			api_keys = json.load(api_keys_file)
		except Exception as e:
			print "The following error occurred. Do you have an api_secrets.json file? %s" % e
			sys.exit()

		try:
			self.GOOGLE_CALENDAR_DEVELOPER_KEY = api_keys['GOOGLE_CALENDAR_DEVELOPER_KEY']
		except Exception as e:
			print 'The following error occurred. We could not process your Google Calendar API key. It should be of format' + \
 					'{ "GOOGLE_CALENDAR_API_KEY": "YOUR API KEY HERE"} \n %s' % e
			sys.exit()

		try:
			self.GOOGLE_CALENDAR_ID = api_keys['GOOGLE_CALENDAR_ID']
		except Exception as e:
			print "The following error occurred: %s" % e
		api_keys_file.close()
		if self.credentials is None or self.credentials.invalid == True:
		  self.credentials = tools.run(FLOW, storage)

	# Create an httplib2.Http object to handle our HTTP requests and authorize it
	# with our good Credentials.
	def createHTTPObject(self):
		http = httplib2.Http()
		self.http = self.credentials.authorize(http)

	# Build a service object for interacting with the API. Visit
	# the Google Developers Console
	# to get a developerKey for your own application.
	def buildServiceObject(self):
		# NEED TO REMOVE ENV DEPENDENCY
		self.service = build(serviceName='calendar', version='v3', http=self.http,
		       developerKey=self.GOOGLE_CALENDAR_DEVELOPER_KEY)


