#!/usr/local/bin/python3

from cgitb import enable
enable()
import pymysql as db
from hashlib import sha256

def dbConnect():
    # Function to open database connection
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

def dbRegisterUser(username, password, display_name, email):
    #Return True if ok, else false
    try:
        sha256_password = sha256(password.encode()).hexdigest()
        connection, cursor=dbConnect()
        cursor.execute("""INSERT INTO ask_users(username, pass, display_name, email)
                                            VALUES (%s, %s, %s, %s)""",
                       (username, sha256_password, display_name, email))
        connection.commit()
        dbClose(connection, cursor)
        return "registered"
    except db.Error:
        return "SERVER_ERROR"
