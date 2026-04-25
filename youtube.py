import os

def task() -> list[str]:
	"""Extracts comments in all files in directories"""
	dirs = [
		"youtube/palworld",
		"youtube/pokemon_arceus",
		"youtube/pokemon_diamond",
		"youtube/pokemon_scarlet",
		"youtube/pokemon_sword",
		"youtube/pokemon_winds",
		"youtube/pokemon_za",
	]
	data = feeder(dirs)

	# Write all extracted comments
	# Go through each post (youtube video)
	for name, post in data.items():
		output_path = f"extracted/{name.replace('/', '')}.txt"
		with open(output_path, "w", encoding="utf-8") as output_file:
			# Go through each comment
			for comment in post:
				output_file.write(comment + "\n")
	return data

def feeder(dirs: list[str]) -> None:
	"""Feeds files into the youtube comment extractor"""
	data = {}
	for dir in dirs:
		data[dir] = [] # organize comments into a post
		for filename in os.listdir(dir):
			file_path = os.path.join(dir, filename)
			if os.path.isfile(file_path): 
				data[dir].extend(youtuber(file_path))
	return data

def youtuber(path: str) -> list[str]:
	"""Extract comments from csv"""
	print(f"Extracting {path}")
	#prefix = '<yt-pdg-comment-chip-renderer id="paid-comment-chip" slot="content" class="style-scope ytd-comment-view-model" hidden="">'
	#prefix = 'class="style-scope ytd-comment-view-model"><span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto" role="text" style="">'
	prefix = '<yt-attributed-string slot="content" id="content-text" class="style-scope ytd-comment-view-model"><span class="ytAttributedStringHost ytAttributedStringWhiteSpacePreWrap" dir="auto" role="text" style="">'
	suffix = "</span>"

	with open(path, "r", encoding="utf-8") as file:
		html = file.read()

	posts = []

	# Scan for posts
	start = 0
	while True:
		start = html.find(prefix, start)
		if start == -1:
			break
		start += len(prefix)
		end = html.find(suffix, start)
		if end == -1:
			break

		# Extract comment
		comment = html[start:end]
		comment = comment.strip()
		comment = comment.replace("\n", "")
		comment = comment.replace("\r", "")
		#print(comment)
		posts.append(comment)

	return posts
