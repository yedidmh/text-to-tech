from flask import Flask, request, render_template
from telapi import rest


app = Flask(__name__)

@app.route('/')
def hello():
	user = { 'name': 'Yedid' }
	return render_template('test_template.html', title = 'Home', user = user)

@app.route('/sms')
def sms():
	sms_body = request.args.get('Body', None)
	
	account_sid = 'ACec889084f5a483fc17fd4115b4be2b5e'
    auth_token = '86b901cc0c16475694d03c8e8bc9523b'
    client = rest.Client(account_sid, auth_token)
    account = client.accounts[client.account_sid]
 
    from_number = request.args.get('To', None)
    to_number = request.args.get('From', None)
    body = "body: " + sms_body 
 
    account.sms_messages.create(from_number, to_number, body)
 
	return "SMS Received"




if __name__ == '__main__':
	app.run()