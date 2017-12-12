from flask import Flask


app = Flask(__name__)


app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world() :
	return "Hello, world!?????!!!!!"


@app.route("/test/<search_query>")
def search(search_query) :
	return search_query


@app.route("/integer/<int:value>")
def int_type(value):
	print (value + 1)
	return "correct"



@app.route("/float/<float:value>")
def float_type(value):
	print (value + 1)
	return "correct"


# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print (value)
	return "correct"


@app.route("/name/<name>")
def index(name) :
	if name.lower() == "dima" :
		return "Hello, {}".format(name), 200
	else :
		return "Not found", 404



if __name__ == '__main__':
	app.run()