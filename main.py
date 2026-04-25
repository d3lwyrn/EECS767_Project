import requests
#import reddit as reddit
import youtube as youtube
import sentiment as sentiment

import words as words

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
	posts = youtube.task()
	print("-- Finished --")

	for name, comments in posts.items():
		print("-- Processing bags of words --")
		wordbags = []
		for comment in comments:
			wordbag = words.generate_bag(comment)
			wordbags.append(wordbag)
			# print(wordbag)
		print("-- Finished --")

		print("-- Extracting youtube comments --")
		sentiment.task(comments, wordbags, True, name.replace("/",""))
		print("-- Finished --")

main()