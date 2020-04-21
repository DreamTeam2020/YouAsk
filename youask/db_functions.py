#!/usr/local/bin/python3

from cgitb import enable
enable()

def dbConnect():
    # Function to open database connection

    from cgi import FieldStorage
    import pymysql as db

    try:
        connection = db.connect('cs1.ucc.ie', 'cgg1', 'weeS2dih', '2021_cgg1')
        cursor = connection.cursor(db.cursors.DictCursor)
        form_data = FieldStorage()
        return connection, cursor, form_data

    except db.Error:
        # If an error occurs return an error code such that the function can handle the error
        connection = "error"
        cursor = ""
        form_data = ""
        return connection, cursor, form_data

def dbClose(connection, cursor):
    cursor.close()
    connection.close()

def pageStart(title, id):
    # This will generate the start of each html page including the <head></head>

    result = """
        <!DOCTYPE html>
        <html lang="en" id="%s">
            <head>
                <meta charset="utf-8" />
                <title>%s - YouAsk</title>
                <link rel="stylesheet" href="styles/styles.css" />
                <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
            </head>
    """ % (id, title)
    return result

def pageEnd():
    # This will generate the end of each html page, including the <footer>

    result = """
                <footer>
                    <p>footer test</p>
                </footer>
            </body>
        </html>"""

    return result