from cgi import FieldStorage
from controller.ctrl_cache import *
from controller.html_functions import loginToAccess, generateQuestionsDisplay
from model.model_functions import getSavedQuestions

def controllerSaved():
    page_name = 'saved'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        questions = getSavedQuestions(logged)
        reverse_bool = True

        form_data = FieldStorage()
        if len(form_data) != 0:
            ordering = form_data.getfirst('chk_sorting', '').strip()
            reverse_bool = False if ordering == 'Earliest' else True

        questions = sorted(questions, key=lambda k: k['id'], reverse=reverse_bool)

        result = generateQuestionsDisplay(questions, False)

    return result

