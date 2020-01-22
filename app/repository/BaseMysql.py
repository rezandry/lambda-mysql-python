import pymysql
from app.config.Mysql import Mysql

class BaseMysql:

    __connection = pymysql.connect(host=Mysql.HOST,
                                   user=Mysql.USER,
                                   password=Mysql.PASSWORD,
                                   db=Mysql.DB,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

    def __init__(self):
        if not self.__connection.open:
            self.__connection.ping(reconnect=True)

    def _get_cursor(self):
        return self.__connection.cursor()

    def _close_cursor(self):
        return self.__connection.cursor().close()

    def _close_connection(self):
        self.__connection.close()