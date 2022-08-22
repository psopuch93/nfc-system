#Modify config for your db connection

DB_NAME = "database_name"
SECRET_KEY = 'fr8D!Dhiweb8asad#$SGaasdTRsj4@dea'
DEBUG = True
SQLALCHEMY_POOL_RECYCLE = 30
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="username",
    password="password",
    hostname="hostname",
    databasename="db")
