#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_index import *

enable()

from controller.html_functions import *

page_name = "home"

print('Content-Type: text/html')
print()
result = controllerIndex()

print("""
    %s
    <body>
        %s

        <main>      <!-- The main part of the website --->
            <h1>Home page</h1>
            <button onclick='myFunction()'>Try It</button>
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
            %s
        </aside>

        %s
        %s
    """ % (
pageStart("Home", page_name, False), generateHeader(False), result, generateNav(page_name, False), pageEnd()))
