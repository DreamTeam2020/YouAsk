from db_functions import *
#move import statements into the functions

def registrationValidation(username, password, display_name, email):
    #Validate input on registration

    userResult=usernameValidationRegister(username)
    passResult=passwordValidation(password)
    displayResult=displayNameValidation(display_name)
    emailResult=emailValidation(email)

    return userResult, passResult, displayResult, emailResult

def loginValidation(username, password):
    #Validate input on login
    #Allow the user to enter an email or username

    username_email=emailValidation(username)

    if username_email=='clear':
        userResult="clear"
    else:
        userResult=usernameValidationLogin(username)

    passResult=passwordValidation(password)

    return userResult, passResult


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
        result='Display name cannot include profanity'
    return result

def usernameValidationLogin(username):
    #Validate username
    result='clear'

    if len(username)<5:
        result='unsafe'
    elif profanityFilter(username, 1)==True:
        result='unsafe'
    else:
        for char in username:
            if char==' ':
                result='unsafe'
                break

    if result=="unsafe":
        result="Username must be longer than 4 characters and cannot include space or profanity"

    return result

def usernameValidationRegister(username):
    import pymysql as db

    #Validate username on registration
    result=usernameValidationLogin(username)

    if result=='clear':
        try:
            connection, cursor=dbConnect()

            if connection=="error":
                result='SERVER_ERROR'
            else:
                #MySQL is case insensitive
                cursor.execute("SELECT * FROM ask_users WHERE username = %s", username)
                if cursor.rowcount > 0:
                    result='Username must be unique'

                dbClose(connection, cursor)

        except db.Error:
            result='SERVER_ERROR'

    return result

def passwordValidation(password):
    #Validate password

    #3 counters for each type, increment when one is seen
    if len(password)<8:
        result='unsafe'
    elif password.islower():
        result='unsafe'
    elif password.isupper():
        result='unsafe'
    else:
        letter_count=0
        num_count=0
        special_count=0
        result='clear'
        for char in password:
            if char.isalpha():
                letter_count+=1
            elif char.isnumeric():
                num_count+=1
            else:
                special_count+=1
        if letter_count==0 or num_count==0 or special_count==0:
            result="unsafe"

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
    #Email Testing
    email = "cristianasd223@gmail.com"
    email_test=emailValidation(email)
    if email_test=="clear":
        print('Email: Tested')
    else:
        print('Email: Error')

    #Password Testing
    password = "yuU123#/#wertfW"
    password_test=passwordValidation(password)
    if password_test=="clear":
        print("Password: Tested")
    else:
        print("Password: Error")
    password="geogitvI67"
    password_test=passwordValidation(password)
    if password_test=="clear":
        print("Password: Error")
    else:
        print("Password: Fail Test Passed")

    #Display Name Testing
    display_name="Cristian"
    display_test=displayNameValidation(display_name)
    if display_test=="clear":
        print("Display_Name: Tested")
    else:
        print(display_test)

    #Username Testing
    username="Horrace321"
    username_test=usernameValidationRegister(username)
    if username_test=="clear":
        print("Username: Tested")
    else:
        print(username_test)

    #Login Testing
    username="Horrace321"
    password="yuU123#/#wertfW"
    user_test, pass_test=loginValidation(username, password)
    if user_test == "clear" and pass_test=="clear":
        print("Login: Tested")
    else:
        print("Login: %s - %s" % (user_test, pass_test))

    username="horrace@mail.com"
    password="yuU123#/#wertfW"
    user_test, pass_test=loginValidation(username, password)
    if user_test == "clear" and pass_test=="clear":
        print("Login: Tested")
    else:
        print("Login: %s - %s" % (user_test, pass_test))

