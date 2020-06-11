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
        %s
        
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>
              
                <main class="col-6 bg-secondary" >   %s  </main>
               
                <aside class="col bg-primary" >.col</aside>
              
            </div>
        </div>
        
        %s
    """ % (pageStart("Home", page_name, False), generateHeader(False), generateNav(page_name, False), result,  pageEnd()))
