from http.cookies import SimpleCookie
from hashlib import sha256
from time import time
from shelve import open
from os import environ

def cookieCreate():

    cookie = SimpleCookie()
    sid = sha256(repr(time()).encode()).hexdigest()
    cookie['UASK'] = sid
    cookie['UASK']['path'] = '/'
    cookie['UASK']['expires'] = 14 * 24 * 60 * 60  # Set cookies to expire in 14 days

    return cookie, sid

def sessionCreate(username, email, display_name, sid):
    session_store = open('session_store/sess_' + sid, writeback=True)
    session_store['authenticated'] = True
    session_store['username'] = username
    session_store['email'] = email
    session_store['display_name'] = display_name
    session_store.close()

def verifyLoggedIn():
    result='UNVERIFIED'
    debug="<h1>Start of verifyLoggedIn</h1>"
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        debug = "<h1>There is a http_cookie_header</h1>"
        cookie.load(http_cookie_header)
        if 'UASK' in cookie:
            debug = "<h1>UASK is in cookie</h1>"
            sid = cookie['UASK'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                debug = "<h1>Session store got authenticated - Username: %s</h1>" % session_store.get('username')
                result=session_store.get('username')
    return result, debug
