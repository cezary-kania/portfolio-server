import os 
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import DevConfig, ProdConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)
db = SQLAlchemy(app)
mail = Mail(app)

@app.before_first_request
def create_tables():
    db.create_all()

from Resources.MessageResource import MessagesListResource, MessageResource
api.add_resource(MessagesListResource, '/message')
api.add_resource(MessageResource, '/message/<int:message_id>')

from Resources.VisitCtrResource import VisitCtrListResource, VisitCtrResource
api.add_resource(VisitCtrListResource, '/visits')
api.add_resource(VisitCtrResource, '/visits/<int:visitsCtr_id>')


if __name__ == "__main__":
    app.run(debug=1, port=5000)
