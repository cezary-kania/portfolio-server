class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'

    #Mail config
    MAIL_SERVER = 'smtp.wp.pl'
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = 'kania-halina@wp.pl'#'flask_mailer@wp.pl'
    MAIL_USERNAME = 'kania-halina@wp.pl'#'flask_mailer@wp.pl'
    MAIL_PASSWORD = 'kruszewianka1'#'Qwerty1234'
    MAIL_USE_SSL = True

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True
    