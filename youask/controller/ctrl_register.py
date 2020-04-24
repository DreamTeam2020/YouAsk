from controller.ctrl_validation import *
from controller.ctrl_cache import *
from hashlib import sha256
import pymysql
from model.model_functions import *

def inputControllerRegistration(username, email, display_name, password1, password2):
    server_error=False
    registered=False
    message_list=["<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>"]

    user_result, email_result, display_result, pass_result = registrationValidation(username, email, display_name, password1)

    if user_result == 'clear' and email_result == 'clear' and display_result == 'clear' and pass_result == 'clear' and password1 == password2:
        try:
            error_check=dbRegisterUser(username, password1, display_name, email.lower())
            if error_check=="SERVER_ERROR":
                server_error=True
            else:
                cookie, sid = cookieCreate()
                sessionCreate(username, email, display_name, sid)
                registered=True
                print(cookie)

        except (db.Error, IOError):
            server_error = True
    else:
        #invoke inputErrorMessage
        if user_result=="SERVER_ERROR" or email_result=="SERVER_ERROR":
            server_error=True
        else:
            message_list=inputErrorMessage(user_result, email_result, display_result, password1, password2, pass_result)

    return registered, server_error, message_list


def inputErrorMessage(user_result, email_result, display_result, password1, password2, pass_result):
    username_msg = "<p> </p>"
    email_msg = "<p> </p>"
    display_msg = "<p> </p>"
    password_msg = "<p> </p>"

    if user_result != 'clear':
        username_msg = user_result

    if email_result != 'clear':
        email_msg = email_result

    if display_result != 'clear':
        display_msg = display_result

    if password1 != password2:
        password_msg = '<p class="error">Passwords Must Match</p> '
    elif pass_result != 'clear':
        password_msg = pass_result

    message_list=[username_msg, email_msg, display_msg, password_msg]
    return message_list