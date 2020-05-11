#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_logout import *

page_name="logout"

result=controllerLogout()

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
    """ % (pageStart("Logout", page_name, False), generateHeader(False), result, generateNav(page_name, False), pageEnd()))



