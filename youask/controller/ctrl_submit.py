from cgi import escape
from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import FieldStorage

def controllerSubmission():
    # Controller for the submit view, verify user input and then submit the question if verified

    url = "submit.py"
    question = ""
    description = ""
    result = loginToAccess()
    error_msg = "<p> </p>"

    # Check if user is logged in
    # If logged in print form then do len form data
    username=verifyLoggedIn(False)   # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        result = generateQuestionForm(url, question, description, error_msg)

        form_data=FieldStorage()

        if len(form_data)!=0:
            question= escape(form_data.getfirst('question', '').strip())
            description = escape(form_data.getfirst('description', '').strip())

            if not question:
                error_msg='<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
            else:
                # Filter out profanity on description, block questions that include profanity
                if len(question) < 5:    # Remove this later for proper verification
                    error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity ' \
                                'within the question. Profanity within the description will be filtered out.</p>'
                else:
                    # If input has been verified then insert the user's question in the database
                    submission_result = submitQuestion(username, question, description)
                    if submission_result=="SERVER_ERROR":
                        error_msg = '<p class="error">Server Error Occurred</p>'
                    else:
                        #Question was submitted
                        question=''
                        description=''
                        error_msg = '<p class="error">Question Has Been Submitted</p>'

            result = generateQuestionForm(url, question, description, error_msg)
    return result
