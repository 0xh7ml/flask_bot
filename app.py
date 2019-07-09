from flask import Flask,request

app = Flask(__name__)

@app.route('/' ,methods = ['GET'])
def verify():
    if request.args.get('hub.mode') == "subscribe" and request.args.get('hub.challange'):
        if not request.args.get('hub.verify_token') == "diyabot":
            return "token mismatch" , 403 
        return request.args["hub.challange"] , 200
    return '<center> <h1> Successfully Run </h1></center>',200


if __name__ == "__main__":
    app.run()
