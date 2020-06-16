from cgi import FieldStorage, escape

from model.model_functions import *
from controller.html_functions import generateQuestionsDisplay
from controller.ctrl_cache import verifyLoggedIn, savePageToSession

def controllerQuestions():
    page_name = 'questions'
    verify_logged = verifyLoggedIn('username', False)

    if verify_logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

    questions = getQuestion()

    form_data = FieldStorage()
    if len(form_data) != 0:
        ordering = escape(form_data.getfirst('chk_sorting', '').strip())

        if ordering == 'Latest':
            questions = sorted(questions, key=lambda k: k['id'], reverse=True)

    result = generateQuestionsDisplay(questions, False)

    return result

if __name__=='__main__':
    questions= getQuestion()

    questions = sorted(questions, key=lambda k: k['id'], reverse=True)
    print(questions)
