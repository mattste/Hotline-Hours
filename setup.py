#!/usr/bin/env python

from distutils.core import setup

setup(name='Hot-Hours',
      version='1.0',
      description='Making checking hours of the Hotline easy',
      author='Matthew Stewart',
      author_email='mattste@umich.edu',
      url='',
      packages=[
      	"docopt",
      	"google-api-python-client",
      	"httplib2",
      	"python-gflags",
      	"pytz",
      	"termcolor",
      	"wsgiref",
      ],
     )