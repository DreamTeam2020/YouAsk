from controller.ctrl_validation import *
from controller.ctrl_cache import *
from cgi import FieldStorage, escape
from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_profile_page import generateProfilePage

def inputControllerLogin():
    user_email=''
    password=''
    error_msg="<p> </p>"
    page_name = 'login'

    verify_logged=verifyLoggedIn('username', False)    # Returns username if logged in else 'UNVERIFIED'
    if verify_logged!="UNVERIFIED":
        savePageToSession(page_name, True)  # Save the current page to the visitor's session store
        error_msg=alreadyLoggedIn()
    else:
        form_data = FieldStorage()
        if len(form_data) != 0:
            server_error=False
            input_error=False

            # Get user input from the form
            user_email = escape(form_data.getfirst('txt_user_email', '').strip())
            password = escape(form_data.getfirst('txt_password', '').strip())

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
                        profile_page=generateProfilePage(result['username'])
                        savePageToSession(page_name, True)  # Save the current page to the visitor's session store
                        error_msg = '<p class="error">Successfully Logged In! ' \
                                    'View your profile page <a href="profile_pages/%s">here</a></p>' % profile_page
                        user_email = ''
                        password = ''
                        print(cookie)

                if server_error:
                    error_msg = '<p class="error">Server Error Occurred</p>'
                elif input_error==True:
                    error_msg = '<p class="error">Invalid Username or Password</p>'

    return user_email, password, error_msg