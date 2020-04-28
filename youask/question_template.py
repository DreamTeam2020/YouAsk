#!/usr/local/bin/python3

from cgitb import enable
enable()

from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_question_page import *

page_name='question'
result, debug=controllerQuestionAnswers(3)


# Add a form to the end so users can answer the question posed


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
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Question", page_name), result, debug, generateNav(page_name), pageEnd()))
