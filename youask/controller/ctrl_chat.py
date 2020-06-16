from cgi import FieldStorage, escape

from controller.html_functions import generateChatForm
from model.model_functions import chatmessage


def controllerchatSubmission(senter, receiver, message):
    server_error = False
    input_error = False
    submitted = False

    submission_result = chatmessage(senter, receiver, message)

    if submission_result == "SERVER_ERROR":
        server_error = True
    else:
        submitted = True

    return submitted, server_error, input_error


def conctrollerchat():
    url = "chat.py"
    page_name = 'chat'
    message = ""
    error_msg = "<p> </p>"

    result = generateChatForm(url, message, error_msg)
    form_data = FieldStorage()
    if len(form_data) != 0:
        message = escape(form_data.getfirst('message', '').strip())
        email = ''

        submitted, server_error, input_error = controllerchatSubmission("CYCYCY4", "Cristian", message)

        if submitted == True:
            error_msg = '<p class="error">message Has Been Submitted</p>'
            description = ''
        elif server_error == True:
            error_msg = '<p class="error">Server Error Occurred</p>'
        elif input_error == True:
            error_msg = '<p class="error">Please ensure there is no profanity in message.</p>'

        result = generateChatForm(url, message, error_msg)
    return result
