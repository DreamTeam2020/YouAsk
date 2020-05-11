#!/usr/local/bin/python3

from cgitb import enable
enable()
import sys
sys.path.append("../")  # Because it's a subdirectory we append this to all of the subsequent imports

from controller.ctrl_question_page import *
from controller.html_functions import *

page_name='question'
result = controllerQuestionAnswers(820399)


# Add a form to the end so users can answer the question posed


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
    """ % (pageStart("Question", page_name, True), generateHeader(True), result, generateNav(page_name, True), pageEnd()))
