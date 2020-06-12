from controller.html_functions import loginToAccess, generateConnectionsDisplay
from controller.ctrl_cache import *

def controllerConnections():
    page_name = 'connections'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store
        result = generateConnectionsDisplay(logged, 0, False)

    return result



if __name__=='__main__':
    result = generateConnectionsDisplay('Cristian', 0, False)
    print(result)
