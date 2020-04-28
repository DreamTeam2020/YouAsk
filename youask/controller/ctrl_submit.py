from cgi import escape
from model.model_functions import *

def controllerSubmission(form_data, username):
    # Controller for the submit view, take in the form_data, verify it and then submit the question if verified
    server_error=False
    input_error=False
    submitted=False

    error_msg = "<p> </p>"

    question= escape(form_data.getfirst('question', '').strip())
    description = escape(form_data.getfirst('description', '').strip())

    if not question:
        error_msg='<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
    else:
        # Filter out profanity on description, block questions that include profanity
        if len(question) < 5:   #Remove this later for proper verification
            input_error=True
        else:
            # If input has been verified then insert the user's question in the database
            submission_result = submitQuestion(username, question, description)
            if submission_result=="SERVER_ERROR":
                server_error=True
            else:
                submitted=True

    return submitted, server_error, input_error, error_msg
