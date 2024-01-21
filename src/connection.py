import mariadb
from datetime import datetime
import sys
import os


def open_db_connection():
    user = os.environ.get("DB_USER")
    passw = os.environ.get("DB_PASS")
    try:
        conn = mariadb.connect(
            user=user, password=passw, host="127.0.0.1", database="properties"
        )
        cur = conn.cursor()
    except mariadb.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
    return conn, cur


def check_and_insert_db(results, table_name):
    new_properties = []
    conn, cur = open_db_connection()
    for result in results:
        cur.execute(
            "SELECT web_key FROM {} WHERE web_key=?".format(table_name),
            (result["id"],),
        )
        if cur.fetchone() == None:
            cur.execute(
                "INSERT INTO {} (web_key, name, address, url, price) VALUES (?,?,?,?,?)".format(
                    table_name
                ),
                (
                    result["id"],
                    result["name"],
                    result["address"],
                    result["link"],
                    result["price"],
                ),
            )
            new_properties.append(result)
        conn.commit()
    conn.close()
    print(
        "Added {0} new {2} properties - {1}".format(
            *[
                len(new_properties),
                datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                table_name,
            ]
        )
    )
    return new_properties
