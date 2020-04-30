#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_cache import *
from controller.ctrl_submit import *
from http.cookies import SimpleCookie
from os import environ
from shelve import open
from cgi import FieldStorage

# Can't submit unless logged in, user enters Question and optional description (Markdown) into form

page_name="submit"
url="submit.py"

question=""
description=""
result = loginToAccess()
error_msg="<p> </p>"

#Check if user is logged in
# If logged in print form then do len form data
verify_login=verifyLoggedIn(False)   # Returns username if logged in, else false

if verify_login!='UNVERIFIED':  # If the user is logged in, print the question submission form
    result=generateQuestionForm(url, question, description, error_msg)

    form_data = FieldStorage()
    if len(form_data)!=0:
        submitted, server_error, input_error, error_msg=controllerSubmission(form_data, verify_login)

        if submitted==True:
            error_msg = '<p class="error">Question Has Been Submitted</p>'
            #Provide link to the question page
        elif server_error==True:
            error_msg = '<p class="error">Server Error Occurred</p>'
        elif input_error==True:
            error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity within the question. ' \
                        'profanity within the description will be filtered out</p>'

        result = generateQuestionForm(url, question, description, error_msg)
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