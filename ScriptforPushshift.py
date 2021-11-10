import urllib.request
import ssl
import csv
import certifi

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


with open("MetacanadaPosts.csv", newline="") as csvfile:
    data = list(csv.reader(csvfile))

    for row in data:

        print('Beginning file download with urllib2...')

        url = 'https://api.pushshift.io/reddit/search/submission/?after=1546300800&subreddit=metacanada&size=1000.json'
        urllib.request.urlretrieve(url, '//Users/nicholaschevrier/Downloads/download1.json')