#!/usr/local/bin/python3

from cgitb import enable
enable()

from html_functions import *
from controller.ctrl_validation import *
from controller.ctrl_cache import *
from controller.ctrl_register import *
from model.model_functions import *
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
import re

page_name = "register"
redirect= "register.py"
username=""
email=""
display_name=""

messageList=["<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>"]
error_msg="<p> </p>"

form_data=FieldStorage()

if len(form_data) !=0:
    server_error=False

    username=escape(form_data.getfirst('username', '').strip())
    email=escape(form_data.getfirst('email', '').strip())
    display_name=escape(form_data.getfirst('display_name', '').strip())
    password1=escape(form_data.getfirst('password1', '').strip())
    password2=escape(form_data.getfirst('password2', '').strip())



    if not username or not email or not display_name or not password1 or not password2:
        error_msg='<p class="error">All Fields Must Be Filled</p>'
    else:
        registered, server_error, messageList=inputControllerRegistration(username, email, display_name, password1, password2)

        if registered==True:
            error_msg = '<p class="error">Successfully Registered! <a href=login.py>Login Here</a></p>'
            redirect = 'registered.py' #Redirect to a different page after registration here
        elif server_error == True:
            error_msg = '<p class="error">Server Error Occurred</p>'
        else:
            messageList=messageList

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
    """ % (pageStart("Register", page_name), redirect, username, messageList[0], email, messageList[1], display_name, messageList[2], messageList[3], error_msg, generateNav(page_name), pageEnd()))
