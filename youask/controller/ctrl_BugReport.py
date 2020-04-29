from cgi import FieldStorage, escape
from model.model_functions import *

def controllerBugreportSubmission(form_data):
    # Controller for the submit view, take in the form_data, verify it and then submit the question if verified
    server_error=False
    input_error=False
    submitted=False

    error_msg = "<p> </p>"
    description = escape(form_data.getfirst('description', '').strip())


    submission_result = BugReport(description)
    if submission_result=="SERVER_ERROR":
                server_error=True
    else:
                submitted=True

    return submitted, server_error, input_error, error_msg

