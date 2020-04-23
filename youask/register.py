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

page_name = "register"
username=""
email=""
display_name=""

username_msg=""
email_msg=""
display_msg=""
password_msg=""
error_msg="<h1>error_msg start point</h1>"
debug_message='<h1>EMPTY</h1>'  #DEBUG - if nothing is received

form_data=FieldStorage()

if len(form_data) !=0:
    server_error=False

    username=escape(form_data.getfirst('username', '').strip())
    email=escape(form_data.getfirst('email', '').strip())
    display_name=escape(form_data.getfirst('display_name', '').strip())
    password1=escape(form_data.getfirst('password1', '').strip())
    password2=escape(form_data.getfirst('password2', '').strip())
    debug_message='<h1>%s</h1>' % username  #DEBUG - if the username is received (it is)

    if not username or not email or not display_name or not password1 or not password2:
        display_result=displayNameValidation(display_name)
        debug_message='<p>DISPLAY_NAME: %s</p>' % display_result #DEBUG - Testing each result

        error_msg='<p class="error">All Fields Must Be Filled</p>'
    else:
        #All return 'clear' if they pass the stipulations
        user_result, email_result, display_result, pass_result = registrationValidation(username, email, display_name, password)

        if user_result == 'clear' and email_result == 'clear' and display_result == 'clear' and pass_result == 'clear' and password1 == password2:
            try:
                connection, cursor=dbConnect()
                if connection=="SERVER_ERROR":
                    server_error=True
                else:
                    sha256_password=sha256(password1.encode()).hexdigest()
                    cursor.execute("""INSERT INTO ask_users(username, pass, display_name, email
                                        VALUES (%s, %s, %s, %s))""", (username, sha256_password, display_name, email.lower()))
                    connection.commit()
                    dbClose(connection, cursor)

                    cookie=SimpleCookie()
                    sid = sha256(repr(time()).encode()).hexdigest()
                    cookie['sid'] = sid
                    session_store = open('sess_'+ sid, writeback=True)
                    session_store['authenticated']=True
                    session_store['username']=username
                    session_store['email']=email
                    session_store['display_name']=display_name
                    session_store.close()
                    error_msg='<p>Successfully Registered!</p>'
                    print(cookie)

            except (db.Error, IOError):
                server_error=True
        else:
            if user_result!='clear':
                if user_result=="SERVER_ERROR":
                    server_error=True
                    #handle server error here
                else:
                    username_msg=user_result
                    print(username_msg)


            if email_result!='clear':
                email_msg=email_result
                print(email_msg)

            if display_result!='clear':
                display_msg=display_result
                print(display_msg)

            if password1!=password2:
                password_msg='<p class="error">Passwords Must Match</p> '
                print(password_msg)
            elif pass_result!='clear':
                password_msg=pass_result
                print(password_msg)

    if server_error==True:
        error_msg = '<p class="error">Server Error Occurred</p>'



print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>HEADER</h1>
        </header>

        <main>      <!-- The main part of the website --->
            <form action="register.py" method="post">
                <fieldset> <!-- Username, Email, Display Name, Password1, Password2 -->
                    <legend>Register</legend>
                    
                    <label for="username">Username: </label>
                    <input type="text" name="username" id="username" value="%s" maxlength="20"/>
                    %s
                    %s
                    <label for="email">Email Address: </label>
                    <input type="text" name="email" id="email" value="%s" maxlength="50"/>
                    %s
                    <label for="display_name">Display Name: </label>
                    <input type="text" name="display_name" id="display_name" value="%s" maxlength="35"/>
                    %s
                    <label for="password1">Password: </label>
                    <input type="password" name="password1" id="password1"/>
                    <label for="password2">Re-Enter Password: </label>
                    <input type="password" name="password2" id="password2"/>
                    %s
                    <input type="submit" value="Register"/>
                </fieldset
            </form>
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Register", page_name), username, username_msg, debug_message, email, email_msg, display_name, display_msg, password_msg, error_msg, generateNav(page_name), pageEnd()))
