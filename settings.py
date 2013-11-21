# -*- coding: utf-8 -*-

class Config(object):
    # Flask core settings
    DEBUG = False 
    SECRET_KEY = '73:65:63:72:65:74:20:6b:65:79'

    # Babel settings
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    BABEL_DEFAULT_TIMEZONE = 'America/Sao_Paulo'

    # MongoKit settings
    MONGODB_DATABASE = 'squid_handler'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017


class ProdutionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    # MongoKit settings
    MONGODB_DATABASE = 'squid_handler_test'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
