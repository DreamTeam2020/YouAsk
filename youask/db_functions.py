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
    # Close existing connections

    cursor.close()
    connection.close()

