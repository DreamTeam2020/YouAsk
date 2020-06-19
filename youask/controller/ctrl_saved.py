from cgi import FieldStorage
from controller.ctrl_cache import *
from controller.html_functions import loginToAccess, generateQuestionsDisplay
from model.model_functions import getSavedQuestions, executeSelectQuery

def controllerSaved():
    page_name = 'saved'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        saved_questions = getSavedQuestions(logged)
        query = 'SELECT * FROM ask_questions WHERE id in ('
        for row in saved_questions:
            query += '%d, ' % row['question_id']
        query = query[:-2]
        query += ')'

        questions = executeSelectQuery(query)   # Returns the fetchall of a given select query

        reverse_bool = True

        form_data = FieldStorage()
        if len(form_data) != 0:
            ordering = form_data.getfirst('chk_sorting', '').strip()
            reverse_bool = False if ordering == 'Earliest' else True

        questions = sorted(questions, key=lambda k: k['id'], reverse=reverse_bool)

        result = generateQuestionsDisplay(questions, False)

    return result


if __name__ == "__main__":
    logged = 'whiskers'

    saved_questions = getSavedQuestions(logged)
    query = 'SELECT * FROM ask_questions WHERE id in ('
    for row in saved_questions:
        query += '%d, ' % row['question_id']
    query = query[:-2]
    query += ')'
    print(query)

    questions = executeSelectQuery(query)  # Returns the fetchall of a given select query

    reverse_bool = True

    questions = sorted(questions, key=lambda k: k['id'], reverse=reverse_bool)

    result = generateQuestionsDisplay(questions, False)
    print(result)
