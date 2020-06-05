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

def verifyLoggedIn(key, sub_dir):    # If sub_dir is true then a view within a subdirectory is calling this function
    # Verifies if the user is logged in and then passes back the value of the given key
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
                result=session_store.get(key)   # Get value from session store based on given key
    return result


def saveToSession(key, value, sub_dir):
    # Save a given key and value to the user's session
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:  # If the user has a http cookie
        cookie.load(http_cookie_header)  # Load the cookies
        if 'UASK' in cookie:  # If this websites cookie is in their list
            sid = cookie['UASK'].value
            session_store = open('%ssession_store/sess_' % prefix + sid, writeback=True)
            session_store[key] = value
            session_store.close()

def getValueFromSession(key, sub_dir):
    # Get value of a given key from user's session
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    result='NOT_FOUND'
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:  # If the user has a http cookie
        cookie.load(http_cookie_header)  # Load the cookies
        if 'UASK' in cookie:  # If this websites cookie is in their list
            sid = cookie['UASK'].value
            session_store = open('%ssession_store/sess_' % prefix + sid, writeback=False)
            result=session_store.get(key)

    return result

def removeKeyFromSession(key, sub_dir):
    # Pop key and value from user's session given the key
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    result='NOT_FOUND'
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:  # If the user has a http cookie
        cookie.load(http_cookie_header)  # Load the cookies
        if 'UASK' in cookie:  # If this websites cookie is in their list
            sid = cookie['UASK'].value
            session_store = open('%ssession_store/sess_' % prefix + sid, writeback=True)
            result=session_store.pop(key)

    return result

def SavePageToSession(page, sub_dir):
    # Save the page the user is on to the session store
    key = 'previous_page'
    saveToSession(key, page, sub_dir)

def getPreviousPageFromSession(sub_dir):
    # Get the previous page the user visited from the session store
    key = 'previous_page'
    result = getValueFromSession(key, sub_dir)
    return result

def saveUserToSession(username, sub_dir):
    # Save the user of the last visited profile page to the session store
    key = 'potential_connection'
    saveToSession(key, username, sub_dir)

def getPotentialConnectionFromSession(sub_dir):
    # Get the potential user connection from the session store
    key = 'potential_connection'
    result = getValueFromSession(key, sub_dir)
    return result
