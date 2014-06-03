#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

# reqs is a list of requirements
reqs = [str(ir.req) for ir in install_reqs]

setup(name='Hot-Hours',
      version='1.0',
      description='Making checking hours of the Hotline easy',
      author='Matthew Stewart',
      author_email='mattste@umich.edu',
      url='',
      install_requires=reqs,
     )
