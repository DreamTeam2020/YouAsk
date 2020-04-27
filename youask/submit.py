#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_cache import *
from http.cookies import SimpleCookie
from os import environ
from shelve import open
from cgi import FieldStorage

# Can't submit unless logged in, user enters Question and optional description (Markdown) into form

page_name="submit"
redirect="submit.py"

question=""
description=""
result = loginToAccess()
error_msg="<p> </p>"

#Check if user is logged in
# If logged in print form then do len form data
verify_login=verifyLoggedIn()

if verify_login==True:  # If the user is logged in, print the question submission form
    result=generateQuestionForm(redirect, question, description, error_msg)



print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>HEADER</h1>
        </header>

        <main>      <!-- The main part of the website --->
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Submit", page_name), result, generateNav(page_name), pageEnd()))