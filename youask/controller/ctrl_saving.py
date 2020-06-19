from controller.ctrl_cache import *
from controller.html_functions import loginToAccess
from model.model_functions import checkSavedQuestion, saveQuestion, unsaveQuestion

def controllerSave():
    result = loginToAccess(False)   # If not logged in display error message
    page_name = 'save'

    verify_logged = verifyLoggedIn('username', False)  # Returns username if logged in else 'UNVERIFIED'

    if verify_logged != 'UNVERIFIED':
        # If logged in then check previous page in session store, if it says user_profile then check the potential connection

        result = '<p class="error">No Save Available</p>'

        previous_page = getPreviousPageFromSession(False)
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        if previous_page == 'question_page':
            potential_save_id = getLastViewedQuestionFromSession(False)  # Returns the id of the last viewed question page
            if potential_save_id != 'NOT_FOUND':
                check_saved = checkSavedQuestion(verify_logged, potential_save_id)
                if not check_saved:
                    # Save the question to table
                    save_result = saveQuestion(verify_logged, potential_save_id)

                    if save_result == 'SERVER_ERROR':
                        result = '<p class="error">Server Error Has Occurred.</p>'
                    else:
                        result = """
                                <section>
                                    <p class="error">Question has been saved. View your saved questions <a href='saved.py'>here</a>.</p>
                                </section>
                            """
                else:
                    # If question was already saved
                    result = """
                            <section>
                                <p class="error">This question was already saved. View your saved questions <a href='saved.py'>here</a>.</p>
                            </section>
                        """

    return result

def controllerUnsave():
    result = loginToAccess(False)   # If not logged in display error message
    page_name = 'unsave'

    verify_logged = verifyLoggedIn('username', False)  # Returns username if logged in else 'UNVERIFIED'

    if verify_logged != 'UNVERIFIED':
        # If logged in then check previous page in session store, if it says user_profile then check the potential connection

        result = '<p class="error">No Unsave Available</p>'

        previous_page = getPreviousPageFromSession(False)
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        if previous_page == 'question_page':
            potential_save_id = getLastViewedQuestionFromSession(False)  # Returns the id of the last viewed question page
            if potential_save_id != 'NOT_FOUND':
                check_saved = checkSavedQuestion(verify_logged, potential_save_id)
                if check_saved:
                    # Unsave the question
                    save_result = unsaveQuestion(verify_logged, potential_save_id)

                    if save_result == 'SERVER_ERROR':
                        result = '<p class="error">Server Error Has Occurred.</p>'
                    else:
                        result = """
                                <section>
                                    <p class="error">Question has been unsaved. View your saved questions <a href='saved.py'>here</a>.</p>
                                </section>
                            """
                else:
                    # If question wasn't previously saved
                    result = """
                            <section>
                                <p class="error">This question was not previously saved. View your saved questions <a href='saved.py'>here</a>.</p>
                            </section>
                        """

    return result
