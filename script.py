"""Hotline Hours Calculator

Usage: hours
  hours <uniqname> <startDate> <endDate>
  hours [--list=<uniqnames.txt>] <startDate> <endDate>
  hours (-h | --help)
  hours --version

Options:
  [<uniqnames.txt>]  Provide a list of uniqnames to run through. See sample_uniqnames.txt format.
  -h --help  Show this screen.
  --version  Show version.
  <startDate>  Should be of format MM-DD-YY
  <endDate>  Should be of format MM-DD-YY
"""

import re
from datetime import datetime, timedelta
import sys
import json

from docopt import docopt
from termcolor import colored

from utils.config import Configure
from tools.calendar import Calendar

def main():
  arguments = docopt(__doc__, version='Hot Hours Version 1.0')
  print(arguments)

  # Verify dates are of correct format
  try:
    dateRangeStart = datetime.strptime(arguments['<startDate>'], "%m-%d-%y")
    dateRangeEnd = datetime.strptime(arguments['<endDate>'], "%m-%d-%y")
    dateRangeEnd = dateRangeEnd + timedelta(hours=24)
  except ValueError as error:
    print(error)
    sys.exit()

  config_obj = Configure()
  config_obj.setup()
  config_obj.createHTTPObject()
  config_obj.buildServiceObject()

  calendar_obj = Calendar(configuration=config_obj)
  
  events = calendar_obj.eventsByDateRange(dateRangeStart, dateRangeEnd)

  uniqnames = []
  # Run through list of given uniqnames
  if (arguments['--list'] != None):
    with open(arguments['--list']) as f:
      uniqnames = sorted(f.read().splitlines(), key=str.lower)
  else:
    uniqnames.append(arguments['<uniqname>'])

  for uniqname in uniqnames:

    print colored("Running time for %s" % uniqname, 'red')
    uniqname_events = calendar_obj.eventsByUniqname(uniqname=uniqname, events=events)
  
    date = dateRangeStart
    delta = timedelta(days=1)
    while date < dateRangeEnd:
        # ignore Saturday and Sunday
        if (date.weekday() != 5 and date.weekday() != 6):
          date_events_by_uniqname = calendar_obj.eventsByDate(events=uniqname_events, date=date)
          time = calendar_obj.totalEventsTime(events=date_events_by_uniqname)
          if time != 0.00:
            print colored('{:<6}  {:>10}'.format(date.strftime("%m-%d"), date.strftime("%A")) + " hours: ", 'magenta') + colored("%.2f" % time, 'cyan')

        date += delta



if __name__ == '__main__':
  main()