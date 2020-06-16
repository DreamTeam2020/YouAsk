from cgi import FieldStorage
from controller.ctrl_cache import *
from controller.html_functions import loginToAccess, generateSubmissionsDisplay

def controllerSubmissions():
    page_name = 'submissions'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        reverse_bool = True
        form_data = FieldStorage()
        if len(form_data) != 0:
            ordering = form_data.getfirst('chk_sorting', '').strip()
            reverse_bool = False if ordering == 'Earliest' else True

        result = generateSubmissionsDisplay(logged, 0, reverse_bool, False)

    return result


if __name__ == "__main__":
    result = generateSubmissionsDisplay('Cristian', 0, False, False)
    print(result)
