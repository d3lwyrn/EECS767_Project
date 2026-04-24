import requests
#import reddit as reddit
import youtube as youtube

import bag as bag

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
	comments = youtube.task()
	print("-- Finished --")

	print("processing bags of words")
	for comment in comments:
		wordbag = bag.generate_bag(comment)
		print(wordbag)
	print()

main()