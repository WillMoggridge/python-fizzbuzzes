from setuptools import setup, find_packages
import os
import sys

version = '0.1'

setup(name='fizzbuzzes',
      version=version,
      description="Return fizzbuzz from a variety of methods!",
      long_description="""\
      Return FizzBuz created by a variety of methods!
      This is mostly a fun project to have fun with Python.
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='fizz buzz fizzbuzz',
      author='Will Moggridge',
      author_email='will@willmoggridge.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
