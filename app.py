from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello from FastCGI via IIS!"
if __name__ == "__main__":
	app.run()

 # This is from NITINPC
 # This is from AxtriaPC 