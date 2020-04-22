#!/usr/local/bin/python3

from cgitb import enable
enable()

from html_functions import *
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
from py_functions_validation import *
import pymysql as db

page_name = "register"
username=""
email=""
display_name=""

username_msg=""
email_msg=""
display_msg=""
password_msg=""
error_msg=""

form_data=FieldStorage()

if len(form_data) !=0:
    username=escape(form_data.getfirst('username', '').strip())
    email=escape(form_data.getfirst('email', '').strip())
    display_name=escape(form_data.getfirst('display_name', '').strip())
    password1=escape(form_data.getfirst('password1', '').strip())
    password2=escape(form_data.getfirst('password2', '').strip())

    if not username or not  email or not display_name or not password1 or not password2:
        error_msg='<p class="error">All Fields Must Be Filled</p>'
    else:
        #All return 'clear' if they pass the stipulations
        user_result, email_result, display_result, pass_result = registrationValidation(username, email, display_name, password)

        #if all clear then do try except
        #else if statement for each result and let msg equal result

        if user_result == 'clear' and email_result == 'clear' and display_result == 'clear' and pass_result == 'clear' and password1 == password2:
            try:
                #..
            except:
                #...
        else:
            #handle equal passwords next to pass validation

            if user_result!='clear':
                username_msg=user_result





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
    """ % (pageStart("Register", page_name), username, username_msg, email, email_msg, display_name, display_msg, password_msg, error_msg, generateNav(page_name), pageEnd()))
