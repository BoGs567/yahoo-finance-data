from distutils.core import setup
setup(
  name = 'yahoo-finance-data',         # How you named your package folder (MyLib)
  packages = ['yahoo-finance-data'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Retreive data (quote, historical, financial, statistics) from Yahoo Finance.',   # Give a short description about your library
  author = 'Sophocles',                   # Type in your name
  author_email = 'nikitidis567@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/BoGs567/Financial_Data_Base',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/BoGs567/Financial_Data_Base/archive/refs/tags/0.0.1.tar.gz',   
  keywords = ['Yahoo', 'finance', 'data', 'scraper', 'Financial'],   # Keywords that define your package best
  install_requires=['certifi','urllib3','bs4','datetime','selenium',],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'      #Specify which pyhton versions that you want to support
  ],
)