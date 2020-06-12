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
        %s
        
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>
              
                <main class="col-6 bg-secondary" >   %s  </main>
               
                %s
            </div>
        </div>
        
        %s
    """ % (pageStart("Submit", page_name, False), generateHeader(False),  generateNav(page_name, False), result, generateAsideRight(False), pageEnd()))
