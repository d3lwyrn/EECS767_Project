import os

def task() -> None:
	dirs = [
		"reddit/pokemon/"
	]
	data = []
	for dir in dirs:
		for filename in os.listdir(dir):
			file_path = os.path.join(dir, filename)
			if os.path.isfile(file_path): 
				data.extend(redditor(file_path))

	output_path = "text.txt"
	with open(output_path, "w", encoding="utf-8") as output_file:
		for post in data:
			output_file.write(post + "\n")

def redditor(path: str) -> list[str]:
	prefix = "<article class=\"w-full m-0\" aria-label=\""
	suffix = "\""

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

		comment = html[start:end]
		print(comment)
		posts.append(comment)

	return posts
