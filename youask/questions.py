#!/usr/local/bin/python3

from cgitb import enable

from model.model_functions import getQuestion

enable()

from controller.html_functions import *

list1 = []
page_name = "questions"
result = getQuestion()
length = len(result)
questions = ''
for x in result:
    questions += '<p>%s</p>' % x

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
         <link rel="stylesheet" type="text/css" href="../youask/styles/styles.css">

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
