from controller.html_functions import *
from controller.ctrl_cache import *

def controllerConnections():
    page_name = 'connections'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store
        