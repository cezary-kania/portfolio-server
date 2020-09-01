from flask_restful import Resource, reqparse, fields, marshal, abort
from flask_mail import Message 
from datetime import date
message_fields = {
    'Id' : fields.Integer(attribute='id'),
    'Date' : fields.String(attribute='date'),
    'E-mail' : fields.String(attribute='sender_email'),
    'Title' : fields.String(attribute='title'),
    'Message' : fields.String(attribute='message')
}

class MessagesListResource(Resource):
    def post(self):
        from Models.MessageModel import MessageModel
        from app import mail
        parser = reqparse.RequestParser()
        parser.add_argument('e-mail', help = 'e-mail can\'t be blank', required = True, location = 'json')
        parser.add_argument('title', help = 'title can\'t be blank', required = True, location = 'json')
        parser.add_argument('message','message can\'t be blank', required = True, location = 'json')
        data = parser.parse_args()
        new_message = MessageModel(
            date = str(date.today()),
            sender_email = data['e-mail'],
            title = data['title'],
            message = data['message']
        )
        try:
            new_message.save_message()
            message = MessageModel.message_to_mailMSG(new_message)
            mail.send(message)
            return marshal(new_message, message_fields, envelope='Sent message'), 200
        except Exception as e:
            abort(500, message = f'message send error {str(e)}')
    def get(self):
        from Models.MessageModel import MessageModel
        messages = MessageModel.get_all_messages()
        return marshal(messages, message_fields, envelope='Messages'), 200

class MessageResource(Resource):
    def get(self, message_id):
        from Models.MessageModel import MessageModel
        message = MessageModel.get_message(message_id)
        if message is None:
            abort(400, message='Invalid message id')
        return marshal(message, message_fields, envelope='Message'), 200
    def delete(self, message_id):
        from Models.MessageModel import MessageModel
        message = MessageModel.delete_message(message_id)
        if message is None:
            abort(500, message='Error on deleting')
        return marshal(message, message_fields, envelope='Deleted message'), 200
