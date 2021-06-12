#from distutils.core import setup
from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'yahoo-finance-data',         # How you named your package folder (MyLib)
  #packages = ['yahoo-finance-data'],   # Chose the same as "name"
  packages=find_packages(exclude=["contrib", "docs", "tests*"]),
  long_description=long_description,
  long_description_content_type='text/markdown',
  version = '0.0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Retreive data (quote, historical, financial, statistics) from Yahoo Finance.',   # Give a short description about your library
  author = 'Sophocles',                   # Type in your name
  author_email = 'nikitidis567@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/BoGs567/yahoo-finance-data',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/BoGs567/yahoo-finance-data/archive/refs/tags/0.0.5.tar.gz',   
  keywords = ['Yahoo', 'finance', 'data', 'scraper', 'Financial'],   # Keywords that define your package best
  install_requires=['certifi','urllib3','beautifulsoup4','datetime','selenium',],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'      #Specify which pyhton versions that you want to support
  ],
)