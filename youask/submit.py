#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.ctrl_submit import *

# Can't submit unless logged in, user enters Question and optional description (Markdown) into form

page_name="submit"

result=controllerSubmission()

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
    """ % (pageStart("Submit", page_name, False), generateHeader(False), result, generateNav(page_name, False), pageEnd()))
