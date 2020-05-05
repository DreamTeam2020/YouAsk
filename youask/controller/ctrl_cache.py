from http.cookies import SimpleCookie
from hashlib import sha256
from time import time
from shelve import open
from os import environ

def cookieCreate():
    # Generate a cookie to be used
    cookie = SimpleCookie()
    sid = sha256(repr(time()).encode()).hexdigest()
    cookie['UASK'] = sid
    cookie['UASK']['path'] = '/'
    cookie['UASK']['expires'] = 14 * 24 * 60 * 60  # Set cookies to expire in 14 days

    return cookie, sid

def sessionCreate(username, email, display_name, sid):
    # Create a session for the user
    session_store = open('session_store/sess_' + sid, writeback=True)
    session_store['authenticated'] = True
    session_store['username'] = username
    session_store['email'] = email
    session_store['display_name'] = display_name
    session_store.close()

def verifyLoggedIn(sub_dir):    # If sub_dir is true then a view within a subdirectory is calling this function
    # Verify if the user is already logged in
    result='UNVERIFIED'
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:  # If the user has a http cookie
        cookie.load(http_cookie_header)    # Load the cookies
        if 'UASK' in cookie:    # If this websites cookie is in their list
            sid = cookie['UASK'].value
            if sub_dir:
                session_store = open('../session_store/sess_' + sid, writeback=False)  # Open the user's session
            else:
                session_store = open('session_store/sess_' + sid, writeback=False)  # Open the user's session
            if session_store.get('authenticated'):  # If the session is authenticated then they're logged in
                result=session_store.get('username')
    return result

def verifyLoggedInEmail(sub_dir):    # If sub_dir is true then a view within a subdirectory is calling this function
    # Verify if the user is already logged in
    result='UNVERIFIED'
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:  # If the user has a http cookie
        cookie.load(http_cookie_header)    # Load the cookies
        if 'UASK' in cookie:    # If this websites cookie is in their list
            sid = cookie['UASK'].value
            if sub_dir:
                session_store = open('../session_store/sess_' + sid, writeback=False)  # Open the user's session
            else:
                session_store = open('session_store/sess_' + sid, writeback=False)  # Open the user's session
            if session_store.get('authenticated'):  # If the session is authenticated then they're logged in
                result=session_store.get('email')
    return result
