from cgi import FieldStorage, escape

from model.model_functions import dbConnect, dbClose, questionsearch


def searchkeyword():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('search', '').strip())
    fetch=" "
    result=" "
    if len(form_data) != 0:
        fetch=questionsearch(form_data)
    for x in fetch:
        result += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s </section>' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"])
    return result


