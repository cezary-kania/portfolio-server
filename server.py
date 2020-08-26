from flask import Flask, request
from flask_cors import CORS, cross_origin

from Models.Visit import Visit
from Models.Message import Message

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Messages
@cross_origin()
@app.route('/new_message', methods=['POST'])
def new_message():
    message = Message.Save_message(request)
    return message
    
@app.route('/get_all_messages', methods=['GET'])
def get_all_messages():
    return Message.Get_all_messages()

# Visits 
@cross_origin()
@app.route('/new_visit', methods=['POST'])
def new_visit():
    todayCounter = Visit.Add_new_visit(request)
    return todayCounter

@app.route('/get_all_visits', methods=['GET'])
def get_all_visits():
    return Visit.Get_all_visits()

if __name__ == "__main__":
    app.run(port=1234,debug=True)