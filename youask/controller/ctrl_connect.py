from controller.ctrl_cache import *
from controller.html_functions import loginToAccess
from model.model_functions import checkConnectionWithUser, connectToUser, disconnectFromUser

def controllerConnect():
    result = loginToAccess(False)   # If not logged in display error message
    page_name = 'connect'

    verify_logged=verifyLoggedIn('username', False)    # Returns username if logged in else 'UNVERIFIED'

    if verify_logged!='UNVERIFIED':
        # If logged in then check previous page in session store, if it says user_profile then check the potential connection

        result = '<p class="error">No Connections Available</p>'

        previous_page = getPreviousPageFromSession(False)
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        if previous_page == 'user_profile':
            potential_connection = getPotentialConnectionFromSession(False)
            if verify_logged.lower() != potential_connection.lower() and potential_connection != 'NOT_FOUND':
                check_connection = checkConnectionWithUser(verify_logged, potential_connection)
                if check_connection == 'SERVER_ERROR':
                    result = '<p class="error">Server Error Has Occurred.</p>'
                elif not check_connection:
                    # If they are not already connected then establish a new connection
                    connection_result = connectToUser(verify_logged, potential_connection)

                    if connection_result == 'SERVER_ERROR':
                        result = '<p class="error">Server Error Has Occurred.</p>'
                    else:
                        result = """
                            <section>
                                <p class="error">You are now connected with %s</p>
                            </section>
                        """ % potential_connection
                else:
                    # If they are already connected
                    result = """
                        <section>
                            <p class="error">You are already connected with %s</p>
                        </section>
                    """ % potential_connection

    return result


def controllerDisconnect():
    result = loginToAccess(False)   # If not logged in display error message
    page_name = 'disconnect'

    verify_logged=verifyLoggedIn('username', False)    # Returns username if logged in else 'UNVERIFIED'

    if verify_logged!='UNVERIFIED':
        # If logged in then check previous page in session store, if it says user_profile then check the potential connection

        result = '<p class="error">No Connections Available</p>'

        previous_page = getPreviousPageFromSession(False)
        savePageToSession(page_name, True)  # Save the current page to the visitor's session store

        if previous_page == 'user_profile':
            potential_connection = getPotentialConnectionFromSession(False)
            if verify_logged.lower() != potential_connection.lower() and potential_connection != 'NOT_FOUND':
                check_connection = checkConnectionWithUser(verify_logged, potential_connection)
                if check_connection == 'SEVER_ERROR':
                    result = '<p class="error">Server Error Has Occurred.</p>'
                elif not check_connection:
                    # If they are not already connected then display message
                    result = """
                        <section>
                            <p class="error">You were not connected with %s</p>
                        </section>
                    """ % potential_connection
                else:
                    # If they are connected then disconnect them
                    connection_result = disconnectFromUser(verify_logged, potential_connection)

                    if connection_result == 'SEVER_ERROR':
                        result = '<p class="error">Server Error Has Occurred.</p>'
                    else:
                        result = """
                            <section>
                                <p class="error">You are no longer connected with %s</p>
                            </section>
                        """ % potential_connection

    return result
