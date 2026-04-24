import os
import csv
from datetime import datetime

def task(comments: list, wordbags: list, export: bool = True) -> list:
	# Load identifier words
	neg_words = set(load_words("negative.txt"))
	pos_words = set(load_words("positive.txt"))

	# Get sentiment of every comment
	sentiments = []
	for i in range(0, len(comments)):
		wordbag = wordbags[i]
		comment = comments[i]

		pos_count = 0
		neg_count = 0
		
		# count all occurances of positive and negative words
		for word, count in wordbag.items():
			if word in pos_words:
				pos_count += count
			if word in neg_words:
				neg_count += count

		sentiment = {
			"comment": comment,
			"score": pos_count - neg_count
		}
		sentiments.append(sentiment)

	# Create csv
	if export:
		export_csv(sentiments)

	return sentiments

def load_words(file_path: str) -> list[str]:
	"""Load words from a .txt file. One word per line."""
	words = []

	with open(file_path, "r") as file:
		for line in file:
			word = line.strip()
			if word:
				words.append(word)
	return words

def export_csv(sentiments: list[dict]):
	filename = f"exports/sentiments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

	with open(filename, "w", newline="", encoding="utf-8") as file:
		writer = csv.DictWriter(file, fieldnames=["comment", "score"])
		writer.writeheader()
		for sentiment in sentiments:
			writer.writerow(sentiment)
	print(f"-- Exported {filename} --")