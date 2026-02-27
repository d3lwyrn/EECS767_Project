def task() -> None:
	dirs = [
		"reddit/pokemon/"
	]
	data = []
	for path in dirs:
		data.append(**redditor(path))

	output_path = path.rsplit("/", 1)[0] + "/data"
	with open(output_path, "w", encoding="utf-8") as output_file:
		for post in posts:
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
		posts.append(html[start:end])

	return posts
