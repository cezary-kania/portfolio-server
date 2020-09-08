import os 
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

from config import DevConfig, ProdConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)
cors = CORS(app, resources={r"/*" : {"origins":"*"}})
db = SQLAlchemy(app)
mail = Mail(app)

from Resources.MessageResource import MessagesListResource, MessageResource
api.add_resource(MessagesListResource, '/message')
api.add_resource(MessageResource, '/message/<int:message_id>')

from Resources.VisitCtrResource import VisitCtrListResource, VisitCtrResource
api.add_resource(VisitCtrListResource, '/visits')
api.add_resource(VisitCtrResource, '/visits/<int:visitsCtr_id>')


if __name__ == "__main__":
    app.run()
