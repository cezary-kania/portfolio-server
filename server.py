from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from datetime import date
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route('/new_visit', methods=['POST'])
def new_visit():
    if request.method == 'POST':
        todayCounter = Add_new_visit(request)
        return todayCounter

@cross_origin()
@app.route('/get_visits', methods=['GET'])
def get_visits():
    if request.method == 'POST':
        with open('appdata.json', 'r+') as json_file:
           appdata = json.load(json_file)
           return appdata
@cross_origin()
@app.route('/new_message', methods=['GET', 'POST'])
def new_message():
    if request.method == 'POST':
        message = Save_message(request)
        return message
    else:
        with open('messages.json', 'r+') as json_file:
            messages = json.load(json_file)
            return messages

def Save_message(request)-> dict:
    message = {
        "Date" : str(date.today()),
        "E-mail": request.form['e-mail'],
        "Title": request.form['title'],
        "Message": request.form['message'],
    }
    with open('messages.json', 'r+') as json_file:
        messages = json.load(json_file)
        messages['messages'].append(message)
        json_file.seek(0)
        json.dump(messages,json_file,indent=3)
        json_file.truncate()
    return message
def Add_new_visit(request) -> dict:
    with open('appdata.json', 'r+') as json_file:
        appdata = json.load(json_file)
        visitCounter = appdata['visitCounter']
        today = str(date.today())
        todayCounter = list(filter(lambda dailyCounter: (dailyCounter['date'] == today), visitCounter))
        if len(todayCounter) != 0:
            todayCounter = todayCounter[0]
            todayCounter['amount'] = str(1 + int(todayCounter['amount']))
        else:
            todayCounter = {'date' : today, 'amount' : '1'}
            visitCounter.append(todayCounter)
        json_file.seek(0)
        json.dump(appdata,json_file,indent=3)
        json_file.truncate()
        return todayCounter

if __name__ == "__main__":
    app.run(port=1234,debug=False)