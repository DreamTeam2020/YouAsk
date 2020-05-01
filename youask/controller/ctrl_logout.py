from controller.ctrl_cache import *
from http.cookies import SimpleCookie
from os import environ

def controllerLogout():
    result='<p class="Error">You are not logged in</p>'
    verify_logged=verifyLoggedIn(False)

    if verify_logged!='UNVERIFIED':
        # If the user is logged in, log them out

        cookie=SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE')
        cookie.load(http_cookie_header)
        sid = cookie['sid'].value
        session_store = open('sess_' + sid, writeback=True)
        session_store['authenticated'] = False
        session_store.close()
        result="""
                <p>You are now logged out.</p>
                <p><a href="login.py">Log Back In Here</a></p>"""

    return result
