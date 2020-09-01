import json
from datetime import date
from app import db
from flask_mail import Message

class MessageModel(db.Model):
    
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(20), nullable = False)
    sender_email = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(200), nullable = False)
    message = db.Column(db.String(5000), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_message(self, request = None):
        self.save_to_db()
        if request != None:
            MessageModel.Save_message_to_file(request)
    @staticmethod
    def message_to_mailMSG(message):
        return Message(
                subject=f'[Portfolio msg] - {message.title} from {message.sender_email}',
                recipients=["cezary.kaniaq@gmail.com"],
                body=message.message)
    @staticmethod
    def get_all_messages():
        return MessageModel.query.all()

    @staticmethod
    def get_message(message_id):
        msg = MessageModel.query.filter_by(id = message_id).first()
        return msg
    @staticmethod
    def delete_message(message_id):
        msg = MessageModel.query.filter_by(id = message_id).first()
        try:
            db.session.delete(msg)
            db.session.commit()
            return msg
        except:
            return None
    @staticmethod
    def Get_all_messages_from_file():
        with open('../data/messages.json', 'r+') as json_file:
            messages = json.load(json_file)
            return messages
    
    @staticmethod
    def Save_message_to_file(request)-> dict:
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