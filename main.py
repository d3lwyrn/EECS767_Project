import requests
import reddit as reddit

def get_html(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except:
		return None

def main():
	#get_html()
	print("hey1")
	reddit.task()
	print("hey")

main()