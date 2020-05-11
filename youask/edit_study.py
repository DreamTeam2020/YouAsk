#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_edit_study import *

page_name = "edit_study"
edit=controllerEditStudy()

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
    """ % (pageStart("Fields of Study", page_name, False), generateHeader(False), edit, generateNav(page_name, False), pageEnd()))
