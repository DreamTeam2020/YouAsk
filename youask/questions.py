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
        %s
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>
              
                <main class="col-6 bg-secondary" >             
                  <a href="submit.py" class="btn btn-success">submit your question </a>
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
                    
                <aside class="col bg-primary" >.col</aside>
            </div>
        </div>

       
        %s
    """ % (pageStart("Questions", page_name, False), generateHeader(False), generateNav(page_name, False), questions, pageEnd()))
