import os
import csv
from datetime import datetime

COLUMNS = [
	"comment",
	"raw_score",
	"length",
	"normalized_score",
	"class"
]

CLASSES = {
	"-1": "negative",
	"0": "neutral",
	"1": "positive"
}

def task(comments: list, wordbags: list, export: bool = True, export_name: str = "export") -> list:
	"""Calculates a sentiment score for each comment"""
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

		total_tokens = 0
		
		# count all occurances of positive and negative words
		for word, count in wordbag.items():
			total_tokens += count

			weight = 1 # all words are just weighed to 1 by default

			negated = 0

			# handle negation
			base_word = word
			if word[:3] == "not_":
				negated = -1
				base_word = word[4:]

			# is it postive or negative?
			word_class = 0
			if base_word in pos_words:
				word_class = 1
			if base_word in neg_words:
				word_class = -1
			word_class = word_class*negated
			
			if word_class == 1:
				pos_count += weight*(1/count)
			elif word_class == -1:
				neg_count += weight*(1/count)

		raw_score = pos_count - neg_count
		length = total_tokens
		normalized_score = raw_score / max(length, 0)
		score = normalized_score

		comment_class = 0
		if score > 0:
			comment_class = 1
		elif score < 0:
			comment_class = -1

		sentiment = {
			"comment": comment,
			"raw_score": pos_count - neg_count,
			"length": total_tokens,
			"normalized_score": normalized_score,
			"class": CLASSES.get(str(comment_class))

		}
		sentiments.append(sentiment)

	# Create csv
	if export:
		export_csv(sentiments, export_name)

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

def export_csv(sentiments: list[dict], name: str):
	"""Exports the data so it can be used in our graphs"""
	filename = f"exports/{name}.csv"

	with open(filename, "w", newline="", encoding="utf-8") as file:
		writer = csv.DictWriter(file, fieldnames=COLUMNS)
		writer.writeheader()
		for sentiment in sentiments:
			writer.writerow(sentiment)
	print(f"-- Exported {filename} --")