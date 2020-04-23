from db_functions import *
#move import statements into the functions

def registrationValidation(username, email, display_name, password):
    #Validate input on registration

    user_result=usernameValidationRegister(username)
    pass_result=passwordValidation(password)
    display_result=displayNameValidation(display_name)
    email_result=emailValidation(email)

    return user_result, email_result, display_result, pass_result

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
        return '<p class="error">Invalid email address<p>'


def displayNameValidation(display_name):
    #Validate display name

    result='clear'
    if len(display_name)<5:
        result='<p class="error">Display name must be longer than 4 characters</p>'
    #elif profanityFilter(display_name)==True:
     #   result='<p class="error">Display name cannot include profanity</p>'
    return result

def usernameValidationLogin(username):
    #Validate username
    result='clear'

    if len(username)<5:
        result='unsafe'
    #elif profanityFilter(username)==True:
    #   result='unsafe'
    else:
        for char in username:
            if char==' ':
                result='unsafe'
                break

    if result=="unsafe":
        result='<p class="error">Username must be longer than 4 characters and cannot include space or profanity</p>'

    return result

def usernameValidationRegister(username):
    import pymysql as db

    #Validate username on registration
    result=usernameValidationLogin(username)

    if result=='clear':
        try:
            connection, cursor=dbConnect()

            if connection=="SERVER_ERROR":
                result='SERVER_ERROR'
            else:
                #MySQL is case insensitive
                cursor.execute("SELECT * FROM ask_users WHERE username = %s", username)
                if cursor.rowcount > 0:
                    result='<p class="error">Username must be unique</p>'

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
        result='<p class="error">Passwords must be at least 7 characters long and contain a number, special ' \
                 'character and a mix of upper and lower case letters</p>'

    return result


def profanityFilter(input):
    # Basic profanity filter to be used with usernames.
    # Aside: Lots of issues to be tackled for a fully functional filtering system, basic for now
    '''
    from profanityfilter import ProfanityFilter
    import re
    pf = ProfanityFilter()

    parsed_input = re.sub(r'[^a-zA-Z ]+', '', input)
    return True if pf.is_profane(parsed_input) else False
    '''
    return False

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
    display_name="Cristian"
    email = "cristianasd223@gmail.com"
    password="yuU123#/#wertfW"
    user_test, email_test, display_test, pass_test=registrationValidation(username, email, display_name, password)
    if user_test == "clear" and pass_test=="clear" and display_test == "clear" and email_test == "clear":
        print("Login: Tested")
    else:
        print("Login: %s - %s - %s - %s " % (user_test, email_test, display_test, pass_test))

    username="horrace@mail.com"
    password="yuU123#/#wertfW"
    user_test, pass_test=loginValidation(username, password)
    if user_test == "clear" and pass_test=="clear":
        print("Login: Tested")
    else:
        print("Login: %s - %s" % (user_test, pass_test))
