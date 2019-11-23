class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:zxc@localhost/runaway'
    SECRET_KEY = 'secret'
