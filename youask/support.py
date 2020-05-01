#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_bug_report import controllersupport

enable()

from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import FieldStorage

page_name = "support"
result = controllersupport()

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
