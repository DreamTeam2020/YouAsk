#!/usr/local/bin/python3
from cgi import FieldStorage
from cgitb import enable

from model.model_functions import BugReport

enable()

from controller.html_functions import *

page_name = "support"
url= "support.py"
description=""

result=generateBugreportForm(url,  description)
form_data = FieldStorage()
BugReport(form_data)

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->

        </header>

        <main>      <!-- The main part of the website --->
            <h1>test page</h1>

</h2>
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("Support", page_name), generateNav(page_name), pageEnd()))
