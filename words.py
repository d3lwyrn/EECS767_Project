def generate_bag(string: str) -> dict:
	"""Generate bag of words dict from string."""
	normalized_string = normalize(string)
	tokens = tokenize(normalized_string)

	words = dict()
	for preword in tokens:
		word = words.get(preword, None)
		if word is None:
			words[preword] = 1
		else:
			words[preword] = word + 1
	return words

def normalize(s):
	"""Normalize comment so it can be easily be tokenized later."""
	s = s.strip()

	# Lowercase
	s = s.lower()

	# Remove whitespaces
	s = s.replace("\n", " ")
	s = s.replace("\t", " ")
	while "  " in s:
		s = s.replace("  ", " ")

	# Handle contractions
	s = s.replace("don't", "do not")
	s = s.replace("can't", "can not")
	s = s.replace("won't", "will not")
	s = s.replace("we'll", "we will")
	s = s.replace("n't", " not")

	# remove html tags
	s = strip_html(s)

	# remove punctuation
	s = s.replace("!", "")
	s = s.replace("?", "")
	s = s.replace(".", "")
	s = s.replace(",", "")
	s = s.replace("-", "")

	return s

def strip_html(s):
	"""Remove html tags"""
	result = ""
	tag = False
	for ch in s:
		if ch == "<":
			tag = True
		elif ch == ">":
			tag = False
		elif not tag:
			result += ch
	return result

def tokenize(s):
	""""""
	tokens = s.split(" ")
	tokens.sort()

	return tokens