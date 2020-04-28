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

page_name="Bugreport"
url="Bugreport.py"

description=""
error_msg="<p> </p>"
result=generateBugreportForm(url, description, error_msg)
result = BugReport(description)
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