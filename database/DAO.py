from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto
from model.rotta import Rotta
from model.volo import Volo


class DAO():
    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllVoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM flights"
        cursor.execute(query)

        for row in cursor:
            result.append(Volo(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRotte():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID, COUNT(*), SUM(f.DISTANCE)
                FROM flights f 
                GROUP BY f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID """
        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))
        cursor.close()
        conn.close()
        return result


