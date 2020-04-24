#!/usr/local/bin/python3

from cgitb import enable

enable()

from html_functions import *
from py_functions_validation import *
from db_functions import *
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
import re


page_name = "login"
redirect= "login.py"
user_email=""

error_msg="<p> </p>"

form_data = FieldStorage()

if len(form_data) !=0:
    server_error=False
    input_error=False

    user_email = escape(form_data.getfirst('user_email', '').strip())
    password = escape(form_data.getfirst('password', '').strip())

    if not user_email or not password:
        error_msg='<p class="error">All Fields Must Be Filled</p>'
    else:
        user_result, pass_result=loginValidation(user_email, password)
        user_check=False
        if user_result=='username':
            user_check=True
            user_result='clear'
        elif user_result=='email':
            user_result='clear'
        if user_result!='clear' or pass_result!='clear':
            input_error=True
        else:
            sha256_password = sha256(password.encode()).hexdigest()
            try:
                connection, cursor=dbConnect()

                if connection=='SERVER_ERROR':
                    server_error=True
                else:
                    cursor.execute('SELECT * FROM ask_users WHERE (username=%s OR email=%s) AND password=%s', (user_email, user_email, sha256_password))
                    if cursor.rowcount==0:
                        #input_error=True
                        error_msg = '<p class="error">Rowcount empty</p>'
                    else:
                        error_msg="<p>IT WORKED</p>"
                    '''
                    else:
                        cookie = SimpleCookie()
                        sid = sha256(repr(time()).encode()).hexdigest()
                        cookie['UASK'] = sid
                        cookie['UASK']['path'] = '/'
                        cookie['UASK']['expires'] = 14 * 24 * 60 * 60  # Set cookies to expire in 14 days
                        session_store = open('session_store/sess_' + sid, writeback=True)
                        session_store['authenticated'] = True
                        session_store['username'] = username if user_check==True else session_store['email']=email
                        session_store.close()
                        error_msg = '<p class="error">Successfully Logged In!</p>'
                        redirect = 'profile.py'
                        print(cookie)
                    '''
                    dbClose(connection, cursor)
            except (db.Error, IOError):
                server_error = True

    if server_error==True:
        error_msg = '<p class="error">Server Error Occurred</p>'
    elif input_error==True:
        error_msg = '<p class="error">Invalid Username or Password</p>'


print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>HEADER</h1>
        </header>

        <main>      <!-- The main part of the website --->
            <form action="%s" method="post">
                <fieldset> <!-- Username or Email, Password -->
                    <legend>Log In</legend>

                    <label for="user_email">Username or Email: </label>
                    <input type="text" name="user_email" id="user_email" value="%s" maxlength="50"/>
                    
                    <label for="password">Password: </label>
                    <input type="password" name="password" id="password"/>
                    
                    <input type="submit" value="Log In"/>
                </fieldset
            </form>
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Login", page_name), redirect, user_email, error_msg, generateNav(page_name), pageEnd()))
