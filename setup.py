#!/usr/bin/env python

from setuptools import setup
from stratum import version

setup(name='stratum',
      version=version.VERSION,
      description='Stratum server implementation based on Twisted',
      packages=['stratum',],
      zip_safe=False,
      install_requires=['twisted', 'ecdsa', 'autobahn',]
     )
