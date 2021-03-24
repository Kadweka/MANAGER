import os

class Config:
   '''
   General configuration parent class
   '''

   # simple mde  configurations
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   DATABASE_URL ='postgresql+psycopg2://kadweka:qwerty12@localhost/ma3'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_TRACK_MODIFICATIONS=False

# export DATABASE_URL='postgresql+psycopg2://kadweka:qwerty12@localhost/ma3'

# python3.6 manage.py server
class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   DATABASE_URI ='postgresql+psycopg2://kadweka:qwerty12@localhost/ma3'

class TestConfig(Config):
    DATABASE_URI ='postgresql+psycopg2://kadweka:qwerty12@localhost/ma3'
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/ktown003'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
