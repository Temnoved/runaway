class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:zxc@localhost/runaway'
    SECRET_KEY = 'secret'
    SECURITY_PASSWORD_SALT = 'o3p54oxi84mx0b937761nc003c7c6bcm736xn9c'
    SECURITY_PASSWORD_HASH = 'bcrypt'
