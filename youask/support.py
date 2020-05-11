#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_bug_report import controllerSupport

enable()

from controller.html_functions import *

page_name = "support"
result = controllerSupport()

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        %s
        
        <main>      <!-- The main part of the website --->
            %s
        </main>
        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>
        %s
        %s
    """ % (pageStart("support", page_name, False), generateHeader(False), result, generateNav(page_name, False), pageEnd()))
