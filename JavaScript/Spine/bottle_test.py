from bottle import run, route

@route("/")
def index():
	return "<h1>Hello</h1>"

@route("/login/<login>")
def login(login):
	return "<h1>On the login page" + login + "</h1>"

@route("/posted", method = "GET")
def posted():
	return "<h1>Posted</h1>"


if __name__ == "__main__":
	run(debug = True, reloader = True)