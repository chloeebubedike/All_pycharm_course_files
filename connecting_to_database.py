import mysql.connector


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_all_matching_records(db_name, query, data):
    db_connection = None
    result = None
    try:
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        cur.execute(query, data)
        result = cur.fetchall()
    except Exception:
        print("Failed to do database operations")
    finally:
        db_connection.close()
        return result


# for row in get_all_matching_records("tests", "SELECT * FROM abcreport WHERE Rep = %s AND Total > %s", ('Andrews', 100)):
results = [row for row in get_all_matching_records("tests", "SELECT * FROM abcreport", None)
            if row['Rep'] == "Andrews" and row['Total'] > 100]
print(list(results[0].keys()))
for row in results:
    print(list(row.values()))