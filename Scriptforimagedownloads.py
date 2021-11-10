import urllib.request

CSV_FILE = 'images.csv'

with open(CSV_FILE, 'r') as f:
	lines = f.read().split('\n')
	header = lines[0]

	for line in lines[1:]:
		url, new_name = line.split(',')
		print('Downloading %s...' % url, end='')
		suffix = url.rsplit('.', 1)[1]
		new_filename = new_name + '.' + suffix
		try:
			urllib.request.urlretrieve(url, new_filename)
			print('Success')
		except urllib.error.HTTPError as e:
			print('File Not Found')
