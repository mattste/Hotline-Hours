import sys
import os.path
import json
import pytz
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.config import Configure

def main():
	test = TestConfigure()

class TestConfigure(object):


	def __init__(self):
		self.config_obj = Configure()
		self.test_setup()
		self.test_createHTTPObject()
		self.test_buildServiceObject()
		pass

	def test_setup(self):
		setup = self.config_obj.setup()

	def test_createHTTPObject(self):
		http = self.config_obj.createHTTPObject()

	def test_buildServiceObject(self):
		self.service = self.config_obj.buildServiceObject()


if __name__ == '__main__':
	main()


