#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_edit_profile import *

page_name = "edit_profile"
edit=controllerEditProfile()

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
    """ % (pageStart("Edit Profile", page_name, False), generateHeader(False), edit, generateNav(page_name, False), pageEnd()))
