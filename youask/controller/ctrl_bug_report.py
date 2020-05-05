from cgi import FieldStorage, escape

from controller.ctrl_validation import emailValidationLogin
from controller.html_functions import generateBugreportForm, generateBugreportFormWithEmail
from model.model_functions import *


def controllerBugReportSubmission(form_data, type, description, email):
    # Controller for the submit view, take in the form_data, verify it and then submit the question if verified
    server_error = False
    input_error = False
    submitted = False


    if type == 1:   # User is logged in
        username=verifyLoggedIn(False)
        email=verifyLoggedInEmail(False)
        submission_result = bugReportLogged(description, username, email)

    else:   # User is logged in
        email = emailValidationLogin(email)

        if email == "unsafe":
            input_error = True
            return submitted, server_error, input_error

        submission_result = bugReportNotLogged(description, email)

    if submission_result == "SERVER_ERROR":
        server_error = True
    else:
        submitted = True

    return submitted, server_error, input_error


def controllerSupport():
    result = ''
    url = "support.py"
    email = ""
    description = ""
    error_msg = "<p> </p>"
    verify_login = verifyLoggedIn(False)  # Returns username if logged in, else false

    if verify_login != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        result = generateBugreportForm(url, description, error_msg)

        form_data = FieldStorage()
        if len(form_data) != 0:
            description = escape(form_data.getfirst('description', '').strip())
            email=''

            submitted, server_error, input_error = controllerBugReportSubmission(form_data, 1, description, email)

            if submitted == True:
                error_msg = '<p class="error">Question Has Been Submitted</p>'
                description=''
            elif server_error == True:
                error_msg = '<p class="error">Server Error Occurred</p>'
            elif input_error == True:
                error_msg = '<p class="error">Please ensure there is no profanity in message.</p>'

            result = generateBugreportForm(url, description, error_msg)
    else:
        result = generateBugreportFormWithEmail(url, description, email, error_msg)

        form_data = FieldStorage()

        if len(form_data) != 0:
            description = escape(form_data.getfirst('description', '').strip())
            email = escape(form_data.getfirst('email', '').strip())
            if not description or not email:
                error_msg='<p class="error">All Fields Must Be Filled</p>'
            else:
                submitted, server_error, input_error = controllerBugReportSubmission(form_data, 2, description, email)

                if submitted == True:
                    error_msg = '<p class="error">Question Has Been Submitted</p>'
                    email=''
                    description=''
                elif server_error == True:
                    error_msg = '<p class="error">Server Error Occurred</p>'
                elif input_error == True:
                    error_msg = '<p class="error">Please ensure there is no profanity in the message and that a valid email address has been provided</p>'

            result = generateBugreportFormWithEmail(url, description, email, error_msg)
    return result
