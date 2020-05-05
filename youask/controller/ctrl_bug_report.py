from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn
from controller.ctrl_validation import supportemailvaildation
from controller.html_functions import loginToAccess, generateBugreportForm, generateBugreportFormWithEmail
from model.model_functions import *


def controllerBugreportSubmission(form_data, type):
    # Controller for the submit view, take in the form_data, verify it and then submit the question if verified
    server_error = False
    input_error = False
    submitted = False

    error_msg = "<p> </p>"
    description = escape(form_data.getfirst('description', '').strip())
    email = escape(form_data.getfirst('email', '').strip())
    email = supportemailvaildation(email)
    if(email=="unsafe"):
        submitted=False
        server_error=False
        input_error=True
        return submitted, server_error, input_error, error_msg
    if type == 1:
        submission_result = bugReportOne(description)
    else:
        submission_result = bugReportTwo(description, email)
    if submission_result == "SERVER_ERROR":
        server_error = True
    else:
        submitted = True

    return submitted, server_error, input_error, error_msg


def controllersupport():
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
            submitted, server_error, input_error, error_msg = controllerBugreportSubmission(form_data, 1)

            if submitted == True:
                error_msg = '<p class="error">Question Has Been Submitted</p>'
                # Provide link to the question page
            elif server_error == True:
                error_msg = '<p class="error">Server Error Occurred</p>'
            elif input_error == True:
                error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity within the question. ' \
                            'profanity within the description will be filtered out</p>'

            result = generateBugreportForm(url, description, error_msg)
    else:
        result = generateBugreportFormWithEmail(url, description, email, error_msg)

        form_data = FieldStorage()
        if len(form_data) != 0:
            submitted, server_error, input_error, error_msg = controllerBugreportSubmission(form_data, 2)

            if submitted == True:
                error_msg = '<p class="error">Question Has Been Submitted</p>'
                # Provide link to the question page
            elif server_error == True:
                error_msg = '<p class="error">Server Error Occurred</p>'
            elif input_error == True:
                error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity within the question. ' \
                            'profanity within the description will be filtered out</p>'

            result = generateBugreportFormWithEmail(url, description, email, error_msg)
    return result
