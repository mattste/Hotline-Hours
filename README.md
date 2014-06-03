Hot-Hours
=========

Hot-Hours is a Python script that makes the CAEN Hotline's FTEs annoying task of verifying student hours on Wolverine Access against our Google calendar.

  - Give it a uniqname or a list of uniqnames
  - It'll query the Google Calendar to see how many hours employees have worked
  - Magic


Version
----

1.0

Tech
-----------

Hot-Hours uses a number of open source projects to work properly:

* [docopt] - makes command-line input as easy as it should be
* [Google Python API] - our Google overlords have blessed us with a library
* [gflags] - more Google goodness
* [pytz] - because dealing with timezones makes me wish we never invented the concept of time
* [termcolor] - add some rainbow to your terminal text

Installation
--------------

```sh
virtualenv hotline-hours-venv
source hotline-hours-venv/bin/activate
git clone https://github.com/mattste/Hotline-Hours.git
cd Hotline-Hours
python setup.py install
```

#### Configure API keys

##### Google Calendar
* Head to https://console.developers.google.com
* Register a new project
* Select the project, select "APIs & auth -> APIs" and verify the Calendar API is enabled
* Go to "Credentials" and download your OAuth information. Place the file titled "client_secrets.json" into the project directory
* Copy and paste your API key from "Credentials" into the "sample_google_secrets.json" file
* Find your [calendar ID] and paste that in.
* Rename that file to "google_secrets.json"

Usage
--------------

To find an individual's total hours by uniqname, run the following:
```sh
python script.py uniqname startDate endDate
```
where startDate and endDate are of the form MM-DD-YY

To find a list of individuals' total hours by uniqnames, run the following:
```sh
python script.py --list="sample_uniqnames.txt" startDate endDate
```
See given sample_uniqnames.txt for proper format.

License
----

MIT

[calendar ID]:http://googleappstroubleshootinghelp.blogspot.com/2012/09/how-to-find-calendar-id-of-google.html
