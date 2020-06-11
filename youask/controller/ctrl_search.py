from cgi import FieldStorage, escape

from model.model_functions import questionSearch
from controller.html_functions import generateQuestionsDisplay
from controller.ctrl_cache import verifyLoggedIn, savePageToSession
import datetime


def searchKeyword():
    form_data = FieldStorage()
    txt_search = escape(form_data.getfirst('txt_search', '').strip())
    result = ""
    page_name = 'search'

    verify_logged = verifyLoggedIn('username', False)

    if verify_logged != 'UNVERIFIED':
        savePageToSession(page_name, True)  # Save the current page to the visitor's session store

    if len(form_data) != 0:
        question_result = questionSearch(txt_search)
        if question_result == 'SERVER_ERROR':
            result='<p class="error">Server Error Occurred</p>'
        elif len(question_result) == 0:
            result='<p class="error">No Results Found</p>'
        else:
            result = generateQuestionsDisplay(question_result, False)
            txt_search=''

    return result, txt_search

if __name__=='__main__':
    question_result=[{'id': 17, 'submitter': 'Cristian', 'question': "What's the deal with homelss people?", 'description': 'Just get a house', 'score': 1, 'view_count': 0, 'submission_date': datetime.datetime(2020, 5, 14, 16, 28, 41)}]
    result=generateQuestionsDisplay(question_result, False)
    print(result)