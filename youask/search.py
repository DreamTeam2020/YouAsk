#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_bug_report import controllerSupport
from controller.ctrl_search import searchkeyword

enable()

from controller.html_functions import *

page_name = "search"
result=searchkeyword()

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
    """ % (pageStart("search", page_name, False), result, generateNav(page_name, False), pageEnd()))
