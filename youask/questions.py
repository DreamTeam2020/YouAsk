#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_questions import controllerQuestions

enable()

from controller.html_functions import *


page_name = "questions"
questions = controllerQuestions()


print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->

        </header>


        <main>      <!-- The main part of the website --->
            <h1>test page</h1>
    <a href="sumbit.py">sumbit</a>
        %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("Questions", page_name), questions, generateNav(page_name), pageEnd()))
