from app.repository.BaseMysql import BaseMysql


class UserRepository(BaseMysql):

    def get_user(self, id):
        query = "SELECT " \
            "   biodata.id, biodata.nama " \
            "FROM " \
            "    biodata " \
            "WHERE " \
            "    biodata.id = %s "

        conn = BaseMysql()
        cursor = conn._get_cursor()
        cursor.execute(query, [id])
        result = cursor.fetchone()
        conn._close_cursor()
        conn._close_connection()
        return result

    def get_users(self):
        query = "SELECT " \
            "   biodata.id, biodata.nama " \
            "FROM " \
            "    biodata "

        conn = BaseMysql()
        cursor = conn._get_cursor()
        cursor.execute(query, [id])
        result = cursor.fetchall()
        conn._close_cursor()
        conn._close_connection()
        return result