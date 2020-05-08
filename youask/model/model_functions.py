#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_cache import verifyLoggedIn, verifyLoggedInEmail
import os
import io
enable()
import pymysql as db
from hashlib import sha256
import base64
from PIL import Image
import PIL.Image


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
    try:
        sha256_password = sha256(password.encode()).hexdigest()
        connection, cursor = dbConnect()
        cursor.execute("""INSERT INTO ask_users(username, pass, display_name, email)
                            VALUES (%s, %s, %s, %s)""",
                       (username, sha256_password, display_name, email))
        connection.commit()
        dbClose(connection, cursor)
        return "registered"
    except db.Error:
        return "SERVER_ERROR"


def dbLoginUser(user_email, password):
    try:
        sha256_password = sha256(password.encode()).hexdigest()
        connection, cursor = dbConnect()
        cursor.execute('SELECT * FROM ask_users WHERE (username=%s OR email=%s) AND pass=%s',
                       (user_email, user_email, sha256_password))

        if cursor.rowcount == 0:
            result = "INPUT_ERROR"
        else:
            fetch = cursor.fetchall()
            result = fetch[0]
        dbClose(connection, cursor)
        return result
    except db.Error:
        return "SERVER_ERROR"


def checkAvailability(user_email, data):
    # Takes in the data type (username or email) and the data itself
    # return clear, message or SERVER_ERROR
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_users WHERE %s = %s", (user_email, data))
        if cursor.rowcount > 0:
            result = '<p class="error">%s already in use</p>' % user_email
        else:
            result = 'clear'
        dbClose(connection, cursor)
        return result
    except db.Error:
        return "SERVER_ERROR"

def getUserDetails(username):
    # Takes in username and returns row from table
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_users WHERE username = %s", username)
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch[0]  # Fetch returns a list of dictionaries
    except db.Error():
        return "SERVER_ERROR"

def checkOldPassword(username, old_password):
    # Check if old_password is the same as the user's current password, False if doesn't match
    try:
        sha256_password = sha256(old_password.encode()).hexdigest()
        connection, cursor = dbConnect()
        cursor.execute('SELECT * FROM ask_users WHERE username=%s AND pass=%s', (username, sha256_password))
        if cursor.rowcount == 0:
            return False
        else:
            return True

    except db.Error():
        return "SERVER_ERROR"

def updateUserDisplayName(username, display_name):
    # Update the user's display name
    try:
        connection, cursor = dbConnect()
        cursor.execute('UPDATE ask_users SET display_name=%s WHERE username=%s', (display_name, username))
        connection.commit()
        dbClose(connection, cursor)
        return 'updated'
    except db.Error():
        return 'SERVER_ERROR'

def updateUserPassword(username, password):
    # Update the user's password
    try:
        sha256_password = sha256(password.encode()).hexdigest()
        connection, cursor = dbConnect()
        cursor.execute('UPDATE ask_users SET pass=%s WHERE username=%s', (sha256_password, username))
        connection.commit()
        dbClose(connection, cursor)
        return 'updated'
    except db.Error():
        return 'SERVER_ERROR'


def submitQuestion(username, question, description):
    # Insert question into table and return the id
    try:
        connection, cursor = dbConnect()
        cursor.execute("""INSERT INTO ask_questions(submitter, question, description)
                            VALUES (%s, %s, %s)""", (username, question, description))
        connection.commit()
        dbClose(connection, cursor)
        return cursor.lastrowid
    except db.Error():
        return "SERVER_ERROR"


def submitAnswer(username, answer, question_id):
    try:
        connection, cursor = dbConnect()
        cursor.execute("""INSERT INTO ask_answers(submitter, answer, question_id)
                            VALUES (%s, %s, %s)""", (username, answer, question_id))
        connection.commit()
        dbClose(connection, cursor)
        return "submitted"
    except db.Error():
        return "SERVER_ERROR"


def getSpecificQuestion(id):
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_questions WHERE id=%s", id)
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch[0]  # Fetch returns a list of dictionaries
    except db.Error():
        return "SERVER_ERROR"


def getQuestion():
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_questions")
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch  # Fetch returns a list of dictionaries
    except db.Error():
        return "SERVER_ERROR"


def getAnswers(question_id):
    # This returns a list of answers when given what question they're responding to
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_answers WHERE question_id=%s", question_id)
        if cursor.rowcount > 0:
            result = cursor.fetchall()
        else:
            result = "EMPTY"
        dbClose(connection, cursor)

    except db.Error():
        result = "SERVER_ERROR"
    return result

def getFieldsOfStudy(table_name):
    # Returns all the fields within the provided table
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT DISTINCT field FROM %s" % table_name)
        result = cursor.fetchall()
        dbClose(connection, cursor)
    except db.Error():
        result = "SERVER_ERROR"
    return result




def bugReportLogged(description, submitter, email):
    try:
        connection, cursor = dbConnect()

        cursor.execute("""INSERT INTO ask_support_inbox(submitter, email, message)
                            VALUES (%s,%s,%s)""", (submitter, email, description))
        connection.commit()
        dbClose(connection, cursor)
        return "submitted"
    except db.Error():
        return "SERVER_ERROR"


def bugReportNotLogged(email, description):
    try:
        connection, cursor = dbConnect()

        cursor.execute("""INSERT INTO ask_support_inbox(email, message)
                            VALUES (%s, %s)""", (email, description))
        connection.commit()
        dbClose(connection, cursor)
        return "submitted"
    except db.Error():
        return "SERVER_ERROR"


def questionsearch(form_data):
    connection, cursor = dbConnect()

    cursor.execute("SELECT * FROM ask_questions WHERE question  REGEXP  %s", form_data)
    connection.commit()
    fetch = cursor.fetchall()
    dbClose(connection, cursor)
    return fetch



def uploadpicture(picname):
    connection, cursor = dbConnect()
    opensrc = os.getcwd() + "/images/"+picname
    with open(opensrc, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    cursor.execute("INSERT INTO ask_picture_test(pic) VALUES(%s)",  encoded_string)
    connection.commit()
    dbClose(connection, cursor)
