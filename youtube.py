import os

def task() -> list[str]:
	dirs = [
		"youtube/palworld/"
	]
	data = feeder(dirs)

	# Write all extracted comments
	output_path = "youtube/text.txt"
	with open(output_path, "w", encoding="utf-8") as output_file:
		for post in data:
			output_file.write(post + "\n")
	return data

def feeder(dirs: list[str]) -> None:
	data = []
	for dir in dirs:
		for filename in os.listdir(dir):
			file_path = os.path.join(dir, filename)
			if os.path.isfile(file_path): 
				data.extend(youtuber(file_path))
	return data

def youtuber(path: str) -> list[str]:
	#prefix = '<yt-pdg-comment-chip-renderer id="paid-comment-chip" slot="content" class="style-scope ytd-comment-view-model" hidden="">'
	prefix = 'class="style-scope ytd-comment-view-model"><span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" dir="auto" role="text" style="">'
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
		print(comment)
		posts.append(comment)

	return posts
