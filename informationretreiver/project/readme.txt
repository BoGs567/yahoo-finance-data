This project is intended to demonstrate some applications of data scraping for Yahoo finance.
Scrapers provided here in are intended as examples, they are all extendible (should be extended to fit users purposes).

if not already procured, a webdriver is required for some of the base- scraping modules (selenium based). 
The Chromedriver is recommended (procure it as follows, linux): 
	version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)

	$ wget -qP "/tmp/" "https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip"

	$ sudo mv chromedriver /usr/bin/chromedriver

	$ sudo chown root:root /usr/bin/chromedriver

	$ sudo chmod +x /usr/bin/chromedriver