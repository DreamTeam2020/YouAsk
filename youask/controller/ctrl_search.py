from cgi import FieldStorage, escape

from model.model_functions import dbConnect, dbClose, questionsearch


def searchkeyword():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('search', '').strip())
    fetch=" "
    if len(form_data) != 0:
        fetch=questionsearch(form_data)
    return fetch


