import sys
import os.path
import json
import pytz
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.config import Configure
from tools.calendar import Calendar
from test_config import TestConfigure

def main():
	test = TestCalendar()

class TestCalendar(object):

	def __init__(self):
		self.config_obj = TestConfigure()
		self.calendar_obj = Calendar(self.config_obj.service)
		self.test_eventsByDate()
		self.test_eventsByUniqname()
		self.test_totalEventsTime()
		pass

	def test_eventsByDate(self):
		date = datetime.now()
		events = self.test_eventsByDateRange()
		events = self.calendar_obj.eventsByDate(events, date)
		print json.dumps(events, indent=4)
		return events

	def test_eventsByDateRange(self):
		date = datetime.now()
		events = self.calendar_obj.eventsByDateRange(datetime.now(), datetime.now() + timedelta(days=3))
		return events

	def test_eventsByUniqname(self):
		events = self.test_eventsByDateRange()
		uniqname_events = self.calendar_obj.eventsByUniqname('', events)
		return uniqname_events

	def test_totalEventsTime(self):
		events = self.test_eventsByUniqname()
		time = self.calendar_obj.totalEventsTime(events)
		return time


if __name__ == '__main__':
	main()


