DB_NAME = "database"
SECRET_KEY = 'fr8D!Dhiweb8TRsj4@dea'
DEBUG = True
SQLALCHEMY_POOL_RECYCLE = 30
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="szopenkz",
    password="crewintense",
    hostname="szopenkz.mysql.pythonanywhere-services.com",
    databasename="szopenkz${}".format(DB_NAME))