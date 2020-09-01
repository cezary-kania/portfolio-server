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

import Resources.MessageResource
import Resources.VisitCtrResource

#if __name__ == "__main__":
#    app.run()

# To run: 
# $ FLASK_APP=app.py FLASK_DEBUG=1 flask run 