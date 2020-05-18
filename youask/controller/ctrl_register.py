from controller.ctrl_validation import *
from controller.ctrl_cache import *
from cgi import FieldStorage, escape
from model.model_functions import *
from controller.html_functions import *

def inputControllerRegistration():

    user_details = ["", "", "", "", ""]  # username, email, display_name, password1, password2
    message_list = ["<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>"]  # Contains error messages to be printed

    verify_logged = verifyLoggedIn('username', False)    # Returns username if logged in else 'UNVERIFIED'
    if verify_logged != "UNVERIFIED":
        # If the user is already logged in, prevent them from registering
        message_list[4]=alreadyLoggedIn()
    else:
        form_data=FieldStorage()

        if len(form_data) != 0:
            # Validate and potentially register the user

            server_error=False
            message_list = ["<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>"]   # Message list to contain error messages
            error_msg="<p> </p>"

            # Get the data from the form
            username = escape(form_data.getfirst('txt_username', '').strip())
            email=escape(form_data.getfirst('txt_email', '').strip())
            display_name=escape(form_data.getfirst('txt_display_name', '').strip())
            password1=escape(form_data.getfirst('txt_password1', '').strip())
            password2=escape(form_data.getfirst('txt_password2', '').strip())

            user_details=[username, email, display_name, password1, password2]

            if not username or not email or not display_name or not password1 or not password2:    # If all fields are not filled, return error message
                error_msg='<p class="error">All Fields Must Be Filled</p>'
            else:
                user_result, email_result, display_result, pass_result = registrationValidation(username, email, display_name, password1)   # Validate the user input

                if user_result == 'clear' and email_result == 'clear' and display_result == 'clear' and pass_result == 'clear' and password1 == password2:  # If all fields are validated
                    error_check=dbRegisterUser(username, password1, display_name, email.lower())    # Register the user using the model function

                    if error_check=="SERVER_ERROR":    # If an error occurs set boolean to True
                        server_error=True
                    else:
                        # If the user registers successfully, then make them login
                        user_details = ["", "", "", "", ""]
                        error_msg = '<p class="error">Successfully Registered! <a href=login.py>Login Here</a></p>'
                else:
                    if user_result=="SERVER_ERROR" or email_result=="SERVER_ERROR":
                        server_error=True
                    else:
                        # If it gets to here then there is an issue with one of the fields, check which field and generate the correct error messages
                        message_list=inputErrorMessage(user_result, email_result, display_result, password1, password2, pass_result)

            if server_error:
                error_msg = '<p class="error">Server Error Occurred</p>'

            message_list.append(error_msg)
    return user_details, message_list


def inputErrorMessage(user_result, email_result, display_result, password1, password2, pass_result):
    # Check each field to find which one is incorrect, then assign the appropriate error messages to a list
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
