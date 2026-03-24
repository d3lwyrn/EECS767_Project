import requests
#import reddit as reddit
import youtube as youtube

def get_html(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except:
		return None

def main():
	#get_html()
	#reddit.task()

	print("-- Extracting youtube comments --")
	youtube.task()
	print("-- Finished --")

main()