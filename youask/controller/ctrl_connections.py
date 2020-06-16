from cgi import FieldStorage
from controller.html_functions import loginToAccess, generateConnectionsDisplay
from controller.ctrl_cache import *

def controllerConnections():
    page_name = 'connections'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        reverse_bool = True
        form_data = FieldStorage()
        if len(form_data) != 0:
            ordering = form_data.getfirst('chk_sorting', '').strip()
            reverse_bool = False if ordering == 'Earliest' else True

        result = generateConnectionsDisplay(logged, 0, reverse_bool, False)

    return result


if __name__ == '__main__':
    result = generateConnectionsDisplay('Cristian', 0, False, False)
    print(result)
