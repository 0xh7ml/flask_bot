from flask import Flask

app = Flask(__name__)

@app.route('/')
def eyata():
      return '<center><h1> Hello world </h1></center>'
if __name__ == '__main__':
      app.run()
