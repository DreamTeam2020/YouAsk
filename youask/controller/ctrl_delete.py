from controller.ctrl_cache import *
from controller.html_functions import loginToAccess
from model.model_functions import getSpecificQuestion, deleteAnsweredQuestion, moveCoinsToUser

def controllerDelete():
    result = loginToAccess(False)   # If not logged in display error message
    page_name = 'delete'

    verify_logged=verifyLoggedIn('username', False)    # Returns username if logged in else 'UNVERIFIED'

    if verify_logged!='UNVERIFIED':
        # If logged in then check previous page in session store, if it says user_profile then check the potential connection

        result = '<p class="error">No Deletions Available</p>'

        previous_page = getPreviousPageFromSession(False)
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        if previous_page == 'question_page':
            potential_deletion_id = getLastViewedQuestionFromSession(False)  # Returns the id of the last viewed question page
            if potential_deletion_id != 'NOT_FOUND':
                question = getSpecificQuestion(potential_deletion_id)
                if verify_logged.lower() == question['submitter'].lower() and not question['deleted']:
                    delete_result = deleteAnsweredQuestion(potential_deletion_id)
                    if delete_result == 'SEVER_ERROR':
                        result = '<p class="error">Server Error Has Occurred.</p>'
                    else:
                        coin_move_result = moveCoinsToUser(potential_deletion_id, verify_logged)
                        if coin_move_result == 'SERVER_ERROR':
                            result = '<p class="error">Association has been removed but there was an error when returning your coins.</p>'
                        else:
                            result = """
                                <section>
                                    <p class="error">Your association with this question has been removed.</p>
                                </section>
                            """

    return result
