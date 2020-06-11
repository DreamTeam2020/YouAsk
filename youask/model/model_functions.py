#!/usr/local/bin/python3

from cgitb import enable

import os
import io
enable()
import pymysql as db
from hashlib import sha256
import base64



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

        if cursor.rowcount > 0:
            fetch = cursor.fetchall()
            result = fetch[0]
        else:
            result = "INPUT_ERROR"
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
        return True if cursor.rowcount > 0 else False
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

def getQuestionFields(question_id):
    # Get a question's fields of study given the question id
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT area, field FROM ask_question_fields WHERE question_id=%s", question_id)
        if cursor.rowcount > 0:
            result = cursor.fetchall()
        else:
            result = "EMPTY"
        dbClose(connection, cursor)

    except db.Error():
        result = "SERVER_ERROR"
    return result


def getUserFieldsStudy(username, table_name):
    # Returns all the user's fields within the provided table
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT field FROM %s WHERE username='%s'" % (table_name, username))
        if cursor.rowcount > 0:
            result = cursor.fetchall()
        else:
            result = "EMPTY"
        dbClose(connection, cursor)
    except db.Error():
        result = "SERVER_ERROR"
    return result


def executeInsertQuery(query):
    # Executes a given insert query
    try:
        connection, cursor = dbConnect()
        cursor.execute(query)
        connection.commit()
        dbClose(connection, cursor)
        return "updated"
    except db.Error():
        return "SERVER_ERROR"

def removeFieldsOfStudy(username, table_name):
    try:
        connection, cursor = dbConnect()
        cursor.execute("""DELETE FROM %s WHERE username='%s'""" % (table_name, username))
        connection.commit()
        dbClose(connection, cursor)
        return "removed"
    except db.Error():
        return "SERVER_ERROR"


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


def questionSearch(form_data):
    try:
        connection, cursor = dbConnect()

        cursor.execute("SELECT * FROM ask_questions WHERE question  REGEXP  %s", form_data)
        connection.commit()
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch
    except db.Error():
        return "SERVER_ERROR"

def getPictureCode(username):
    # Get the profile picture from the db given the username
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT picture FROM ask_picture WHERE username=%s", username)

        if cursor.rowcount > 0:
            data = cursor.fetchall()
            result = data[0]['picture']
        else:
            result = 'EMPTY'

        dbClose(connection, cursor)
    except db.Error():
        result = "SERVER_ERROR"

    return result

def uploadProfilePicture(username, encoded_string):
    # Removes the user's old image if there is one, and then uploads new image to database
    try:
        connection, cursor = dbConnect()
        cursor.execute("DELETE FROM ask_picture WHERE username=%s", username)
        connection.commit()

        cursor.execute("INSERT INTO ask_picture(username, picture) VALUES(%s, %s)", (username, encoded_string))
        connection.commit()

        dbClose(connection, cursor)
        return 'submitted'
    except TypeError:
        return "SERVER_ERROR"

def increaseScore(table, id, submitter):
    # Increment score of question/answer in given table using id, then take the submitter and increment their score
    try:
        connection, cursor = dbConnect()
        cursor.execute("""
            UPDATE %s
            SET score = score + 1
            WHERE id='%s'
        """ % (table, id))
        connection.commit()
        cursor.execute("""
            UPDATE ask_users
            SET score = score + 1
            WHERE username='%s'
        """ % (submitter))
        connection.commit()
        dbClose(connection, cursor)
        return "incremented"
    except db.Error():
        return "SERVER_ERROR"

def decrementScore(table, id, submitter):
    # Increment score of question/answer in given table using id, then take the submitter and increment their score
    try:
        connection, cursor = dbConnect()
        cursor.execute("""
            UPDATE %s
            SET score = score - 1
            WHERE id='%s'
        """ % (table, id))
        connection.commit()
        cursor.execute("""
            UPDATE ask_users
            SET score = score - 1
            WHERE username='%s'
        """ % (submitter))
        connection.commit()
        dbClose(connection, cursor)
        return "decremented"
    except db.Error():
        return "SERVER_ERROR"

def connectToUser(username, friend):
    # Given the username of another user, add a row to the friends table
    try:
        connection, cursor = dbConnect()
        cursor.execute("INSERT INTO ask_friends(user, friend) VALUES(%s, %s), (%s, %s)", (username, friend, friend, username))
        connection.commit()
        dbClose(connection, cursor)
        return "connected"
    except db.Error():
        return "SERVER_ERROR"

def disconnectFromUser(username, friend):
    # Given 2 users who are connected, remove their connection
    try:
        connection, cursor = dbConnect()
        cursor.execute("DELETE FROM ask_friends WHERE (user=%s AND friend=%s) OR (user=%s AND friend=%s)", (username, friend, friend, username))
        connection.commit()
        dbClose(connection, cursor)
        return "disconnected"
    except db.Error():
        return "SERVER_ERROR"

def checkConnectionWithUser(username, friend):
    # Given 2 users, check if they're connected
    try:
        connection, cursor = dbConnect()
        cursor.execute("SELECT * FROM ask_friends WHERE user=%s AND friend=%s", (username, friend))
        fetch = cursor.fetchall()
        dbClose(connection, cursor)
        return fetch
    except db.Error():
        return "SERVER_ERROR"
