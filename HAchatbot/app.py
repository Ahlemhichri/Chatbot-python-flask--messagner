from flask import Flask 
from flask import request
import json
from bot import Bot


Salutaion = ['bonjour', 'cv' , 'bonsoir' , 'slm']
app = Flask(__name__)

@app.route('/',methods=['GET' ,'POST' ])
def webhook():
  if request.method == 'GET':
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == 'secret' :
         return str(challenge)
    return '400'
  
  else :
    print (request.data)
    data= json.loads(request.data)
    messaging_events= data['entry'][0]['messaging']
    bot = Bot(PAGE_ACCESS_TOKEN)
    for message in messaging_events:
        user_id = message['sender']['id']
        text_input = message['message'].get('text')
        response_text = 'je suis en train dapprendre'
        if text_input in Salutaion :
             response_text = 'bonjour , bienvenue !'
        print('Message from user ID {} - {}'.format(user_id,text_input))
        bot.send_text_message(user_id , response_text)
    return '200'


if __name__ == '__main__':
  app.run(debug=True)         


