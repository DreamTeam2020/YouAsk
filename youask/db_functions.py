#!/usr/local/bin/python3

from cgitb import enable
enable()

def dbConnect():
    # Function to open database connection

    import pymysql as db

    try:
        connection = db.connect('cs1.ucc.ie', 'cgg1', 'weeS2dih', '2021_cgg1')
        cursor = connection.cursor(db.cursors.DictCursor)
        return connection, cursor

    except db.Error:
        # If an error occurs return an error code such that the function can handle the error
        connection = "SERVER_ERROR"
        cursor = ""
        return connection, cursor

def dbClose(connection, cursor):
    # Close existing connections

    cursor.close()
    connection.close()
