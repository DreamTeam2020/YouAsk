
from model.model_functions import dbConnect, dbClose


def searchkeyword(keyword):
    connection, cursor = dbConnect()

    cursor.execute("SELECT question FROM ask_questions WHERE name REGEXP  %s", keyword)
    connection.commit()
    fetch = cursor.fetchall()
    dbClose(connection, cursor)
    return fetch[0]

