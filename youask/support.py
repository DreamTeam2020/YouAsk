#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_bug_report import controllerBugReportSubmission

enable()

from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import FieldStorage

page_name="Support"
url="support.py"

description=""
error_msg="<p> </p>"

result=generateBugreportForm(url,  description, error_msg)

form_data = FieldStorage()
if len(form_data)!=0:
    submitted, server_error, input_error, error_msg=controllerBugReportSubmission(form_data)

    if submitted==True:
        error_msg = '<p class="error">Question Has Been Submitted</p>'
        #Provide link to the question page
    elif server_error==True:
        error_msg = '<p class="error">Server Error Occurred</p>'
    elif input_error==True:
        error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity within the question. ' \
                    'profanity within the description will be filtered out</p>'

    result = generateBugreportForm(url, description, error_msg)
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
    """ % (pageStart("support", page_name), result, generateNav(page_name), pageEnd()))
