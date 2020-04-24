from controller.ctrl_validation import *
from controller.ctrl_cache import *
from hashlib import sha256
from cgi import FieldStorage, escape
import pymysql
from model.model_functions import *

def inputControllerLogin(form_data):
    server_error=False
    input_error=False
    logged=False

    error_msg="<p> </p>"

    # Get user input from the form
    user_email = escape(form_data.getfirst('user_email', '').strip())
    password = escape(form_data.getfirst('password', '').strip())

    if not user_email or not password:
        error_msg='<p class="error">All Fields Must Be Filled</p>'  # If all fields are not filled
    else:

        user_result, pass_result=loginValidation(user_email, password)  # Validate the user input

        if user_result=='username':
            user_result='clear'
        elif user_result=='email':
            user_result='clear'

        if user_result!='clear' or pass_result!='clear':    # Both inputs must be validated
            input_error=True
        else:
            result=dbLoginUser(user_email, password)    # Attempt to the log the user in

            if result=="INPUT_ERROR":
                input_error=True
            elif result=="SERVER_ERROR":
                server_error=True
            else:
                # Create a cookie and session for the user
                cookie, sid = cookieCreate()
                sessionCreate(result['username'], result['email'], result['display_name'], sid)
                logged=True
                print(cookie)

    return logged, input_error, server_error, user_email, error_msg