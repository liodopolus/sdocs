def app(environ, start_response):
	"""das ist mein Kommentar"""
	data = "Das ist echt eine coole Sache! Was soll ich sagen?\n"
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])

