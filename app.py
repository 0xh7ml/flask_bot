from flask import Flask ,request 
import json 
import requests


pat = 'EAALZB8BN9rOcBAJkNZBNKCo0pZCCp7ObJUvyDpTOwbZCIGjmIj7H94RY9ytRfjJnYhUB9TmyCXPMlhZCrOyReVcjBsBYIb0mC8pOg0LILToCW1uazIVeYcWYVeQBBYUk8MBMpActEKzy2G52tZBZCh9LWUZCOwIy0GfBwZApTzgsdDwZDZD' #here will page axes token 


app = Flask(__name__)
@app.route('/' , methods = ['GET'])
def verify_step():
    if request.args.get('hub.mode') == "subscribe" and request.args.get('hub.challange'):
        if request.args.get('hub.verify_token') != "diyabot":
            return "404 error" , 403
        return request.args['hub.chalange'] , 200
    return 'Hello Saikat,Im Diyabot' ,200

@app.route('/' ,methods = ['POST'])
def handle_msg():
    print "Handling Messages"
    payload = request.get_data()
    print payload
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        send_message(pat, sender, message)
    return "Done !!"
def msg_evnt(payload):
    d = json.loads(payload)
    msg_evnt  = d["entry"][0]["messaging"]
    for event in msg_evnt:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        else:
            yield event["sender"]["id"], "I can't echo this"
def send_message(token, recipient, text):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
                "recipient": {"id": recipient},
                "message": {"text": text.decode('unicode_escape')
                    }}),
            headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text
if __name__ == "__main__":
    app.run
