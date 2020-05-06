
from controller.html_functions import *
from controller.ctrl_cache import *
from model.model_functions import *
from cgi import FieldStorage, escape



def controllerEditProfile():
    # Edit user details, edit fields of study
    # Check if logged in, display the user's current details and a form where they can change them. On submission
    # validate the user input, do error messages then change details in db and session.

    url = "edit_profile.py"
    new_display_name=''
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
            # Generate the form / the user doesnt have to fill the whole form in
            # ( i.e they just want to change display name not password )
            result=generateEditDetailsForm(url, details, new_display_name, old_password, password1, password2, error_messages)
            form_data=FieldStorage()
            if len(form_data)!=0:
                new_display_name= escape(form_data.getfirst('new_display_name', '').strip())
                old_password = escape(form_data.getfirst('description', '').strip())
                password1= escape(form_data.getfirst('password1', '').strip())
                password2 = escape(form_data.getfirst('password2', '').strip())

                # Error messages: if one of the passwords is entered but not the others, call validate on display name,
                # check if old password matches the user if it does then pass1 and 2 must be equal then validate pass 1




def checkErrors(new_display_name, old_password, password1, password2):
    # Check user input for errors
    missing_password=False
    error_messages=['<p> </p>', '<p> </p>', '<p> </p>', '<p> </p>']
    if (old_password and (not password1 or not password2)) or (password1 and (not old_password or not password2)) or (password2 and (not old_password or not password1)):
        missing_password=True
    






