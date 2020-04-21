import pymysql as db
from db_functions import *
import re

#move these into the functions

def loginValidation(username, password, display_name, email):
    # Validate

    userResult=usernameValidation(username)
    passResult=passwordValidation(password)
    displayResult=displayNameValidation(display_name)
    emailResult=emailValidation(email)

    #now do something

def emailValidation(email):
    #Use regular expression to validate email
    import re

    if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return 'clear'
    else:
        return 'Invalid email address'


def displayNameValidation(display_name):
    #Validate display name

    result='clear'
    if len(display_name)<5:
        result='Display name must be longer than 4 characters'
    elif profanityFilter(display_name, 1)==True:
        result='Dsiplay name cannot include profanity'


def usernameValidation(username):
    #Validate username
    result='clear'

    if len(username)<5:
        result='Username must be longer than 4 characters'
    elif profanityFilter(username, 1)==True:
        result='Username cannot include profanity'
    else:
        for char in username:
            if char==' ':
                result='Username cannot include spaces'
                break

    if result=='clear':
        try:
            connection, cursor=dbConnect()

            if connection=="error":
                result='Server temporarily unavailable'
            else:
                #Check this later, sql may be case insensitive
                cursor.execute("SELECT * FROM users WHERE username = %s", username)
                if cursor.rowcount > 0:
                    result='Username must be unique'

                dbClose(connection, cursor)

        except db.Error:
            result='Server temporarily unavailable'

    return result


def passwordValidation(password):
    #Validate password

    if len(password)<8:
        result='unsafe'
    elif password.isalpha():
        result='unsafe'
    elif password.isnumeric():
        result='unsafe'
    elif password.islower():
        result='unsafe'
    elif password.isupper():
        result='unsafe'
    else:
        result='unsafe'
        for char in password:
            if not char.isaplha() and not char.isnumeric():
                result='clear'
                break

    if result=='unsafe':
        result='Passwords must be at least 7 characters long and contain a number, special ' \
                 'character and a mix of upper and lower case letters'

    return result


def profanityFilter(input, check_num):
    # If check_num is 1 then return true or false
    # Else replace profanity with *'s and return replaced text

    if input=="turkey":
        result=True
        return result


if __name__=="__main__":
    email = "cristianasd223@gmail.com"

    if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        print('clear')
    else:
        print('Invalid email address')