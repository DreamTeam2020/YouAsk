from cgi import FieldStorage, escape

from model.model_functions import dbConnect, dbClose


def searchkeyword():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('search', '').strip())
    fetch=" "
    if len(form_data) != 0:

        connection, cursor = dbConnect()

        cursor.execute("SELECT question FROM ask_questions WHERE question  REGEXP  %s", form_data)
        connection.commit()
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch
    return fetch


