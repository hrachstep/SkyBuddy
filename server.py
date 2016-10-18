from flask import Flask, request
import requests
import json

import backend_analytics

app = Flask(__name__)
@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == 'VERIFY_TOKEN':
          return request.args['hub.challenge']
    else:
          return "Error, Invalid Token!"

def reply(user_id, msg):
    ACCESS_TOKEN = 'EAAESYwmugbYBANnRZAu8jDKJPd8aOhZCdk7lJ2Gad1mKZBdZCurOXRghFd21zO7RrnreZCsPeXIs47ZCqFNytLXEqBwW8ybWoUANi6LXeIzlsRnxsa0mm1UEAmZB0Soo91NYdlaI2VdBYOX5iZAPLcNEp1m8Q3AppKaPeFPZBVSIRDwZDZD'
    resp_mess = {
                'recipient': {'id': user_id,},
                'message': {'text': msg,}
                }
    fb_response = requests.post("https://graph.facebook.com/v2.6/me/messages", params={"access_token": ACCESS_TOKEN},
    data=json.dumps(resp_mess), 
    headers = {'content-type': 'application/json'})
    print(fb_response.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json()
    print (data)
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    
    #process message
    print "START TEST"
    print message
    type = backend_analytics.parse_message(message)
    print type
    messageSend = backend_analytics.send_message(type)
    print "END TEST"
    
    reply(sender_id,messageSend)
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1',threaded=True)