
from controller.html_functions import *
from controller.ctrl_cache import *
from model.model_functions import *


def controllerEditProfile():
    # Edit user details, edit fields of study
    # Check if logged in, display the user's current details and a form where they can change them. On submission
    # validate the user input, do error messages then change details in db and session.

    url = "edit_profile.py"
    display_name=''
    old_password=''
    password1=''
    password2=''
    error_messages=['<p> </p>', '<p> </p>', '<p> </p>', '<p> </p>']  # Display name, current password, new password, error msg
    server_error=False

    result = loginToAccess(False)
    username=verifyLoggedIn(False)   # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        # Display user's details and a form where they can be changed

        # Get user's details
        details=getUserDetails(username)
        if details == 'SEVER_ERROR':
            server_error=True
        else:
            # Generate the form / the user doesnt have to fill the whole form in ( i.e they just want to change display name not password)
