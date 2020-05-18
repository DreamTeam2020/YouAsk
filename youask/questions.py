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
        %s


        <main>      <!-- The main part of the website --->
            <h1>test page</h1>
            <a href="submit.py">submit</a>
            <form action="questions.py" method="post">
                <fieldset>
                    <input type="radio" id="chk_earliest" name="chk_sorting" value="Earliest">
                    <label for="chk_earliest">Earliest</label>
                    
                    <input type="radio" id="chk_latest"  name="chk_sorting" value="Latest" checked>
                    <label for="chk_latest">Latest</label>
                    
                    <input type="submit" value="Sort"/>
                </fieldset>
            </form>
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("Questions", page_name, False), generateHeader(False), questions, generateNav(page_name, False), pageEnd()))
