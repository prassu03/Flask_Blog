import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    # MAIL_USE_SSL=False
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    # MAIL_USERNAME='murakalaprasanthi@gmail.com'
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    # MAIL_PASSWORD='gkma elen ifjm udap'

    # print("Loaded Config:")
    # print("SQLALCHEMY_DATABASE_URI =", os.environ.get('SQLALCHEMY_DATABASE_URI'))
    # print("SECRET_KEY =", os.environ.get('SECRET_KEY'))

