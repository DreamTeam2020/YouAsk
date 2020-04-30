#!/usr/local/bin/python3

from cgitb import enable

from model.model_functions import getQuestion

enable()

from controller.html_functions import *

list1 = []
page_name = "questions"
result = getQuestion()
length = len(result)

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->

        </header>


        <main>      <!-- The main part of the website --->
            <h1>test page</h1>
           """ % pageStart("Questions", page_name))
for x in result:
    print(""" <p> %s </p>""" % x)
print("""          %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % generateNav(page_name), pageEnd())
