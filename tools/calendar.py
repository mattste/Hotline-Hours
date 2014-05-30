import json
import pytz
from datetime import datetime, timedelta

from utils import config


class Calendar(object):
	'''
	Given a configuration object, interacts with Google Calendar API
	'''
	EST_tz = pytz.timezone('US/Eastern')

	def __init__(self, configuration):
		self.configuration = configuration


	# Takes any datetime.datetime object and converts
	# it to the nearest day without the hour and minutes
	def _timeToNearestDay(self, date):
		timeMin = datetime(year=date.year, month=date.month, day=date.day, tzinfo=self.EST_tz)
		return timeMin

	# Takes a string format from Google Calendar API and returns
	# a datetime.timedifference object
	def _stringToTime(self, time):
		time = time[:-6]
		time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S')
		return time

	# Return events for a specific date from a list of events
	# date must be formatted as a datetime.timedelta object
	def eventsByDate(self, events, date):
		date_events = []
		for event in events:
			event_time = self._stringToTime(event['start']['dateTime'])
			# print "EVENT_TIME: %s, date: %s" % (event_time, date)
			if event_time.date() == date.date():
				date_events.append(event)
		return date_events

	# Return events for a specific date range
	# dateRangeStart and dateRangeEnd both must be datetime.datetime objects
	def eventsByDateRange(self, dateRangeStart, dateRangeEnd):
		timeMin = self._timeToNearestDay(dateRangeStart)
		timeMin = timeMin.isoformat()
		timeMax = self._timeToNearestDay(dateRangeEnd)
		timeMax = timeMax.isoformat()

		# print "timeMin: %s timeMax: %s" % (timeMin, timeMax)

		events = self.configuration.service.events().list(calendarId=self.configuration.GOOGLE_CALENDAR_ID,
					singleEvents=True,
					timeMin=timeMin, timeMax=timeMax).execute()
		return events

	# Return all events by a given uniqname from an events object
	# events must follow proper Google Calendar API formatting
	def eventsByUniqname(self, uniqname, events):
		uniqname_events = []
		for event in events['items']:
			# verify summary matches uniqname by removing everything following whitespace
			summary = event['summary'].split()[0]
			if summary == uniqname:
				uniqname_events.append(event)
		return uniqname_events

	# Returns the time length of the events
	# Ex. Monday, 9-11 A.M. + 1-3:00pm returns 4
	def totalEventsTime(self, events):
		time = 0.0
		for event in events:
			end_time = event['end']['dateTime']
			# remove final characters used for timezone in request
			end_time = self._stringToTime(end_time)
			
			start_time = event['start']['dateTime']
			start_time = self._stringToTime(start_time)

			diff = end_time - start_time
			time += float(diff.total_seconds()/3600.0)

		return time
