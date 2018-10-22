import pymysql

pymysql.install_as_MySQLdb()

HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE
)