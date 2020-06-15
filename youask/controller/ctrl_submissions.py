from controller.ctrl_cache import *
from controller.html_functions import loginToAccess, generateSubmissionsDisplay

def controllerSubmissions():
    page_name = 'submissions'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store
        result = generateSubmissionsDisplay(logged, 0, False)

    return result


if __name__ == "__main__":
    result = generateSubmissionsDisplay('Cristian', 0, False)
    print(result)