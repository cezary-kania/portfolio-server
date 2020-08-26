import json
from datetime import date

class Message:
    
    @staticmethod
    def Get_all_messages():
        with open('messages.json', 'r+') as json_file:
            messages = json.load(json_file)
            return messages
    
    @staticmethod
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