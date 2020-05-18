from cgi import FieldStorage, escape

from model.model_functions import questionSearch
from controller.html_functions import generateQuestionsDisplay


def searchKeyword():
    form_data = FieldStorage()
    txt_search = escape(form_data.getfirst('txt_search', '').strip())
    result = ""

    if len(form_data) != 0:
        question_result = questionSearch(txt_search)
        if question_result == 'SERVER_ERROR':
            result='<p class="error">Server Error Occurred</p>'
        elif len(question_result) == 0:
            result='<p class="error">No Results Found</p>'
        else:
            result = generateQuestionsDisplay(question_result)

    return result
