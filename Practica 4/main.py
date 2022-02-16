from flask import Flask 

myapp = Flask(__name__)

@app.route('/')
def lev_api():
    return "Hello this is my api"

if __name__ == '__main__':
    myapp.run(host = "0.0.0.0", debug = True)