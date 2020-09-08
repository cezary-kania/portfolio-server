import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'

    #Mail config
    MAIL_SERVER = ''
    MAIL_PORT = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = '' 

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://aduyerpslciqjy:74580de66a5f7b9cfa68da7440ee62135c36c148441ec59b51b13ceb196a5db0@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/dadsaj7o5qrk1k'
    DEBUG = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True
    
