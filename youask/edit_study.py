#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_edit_study import *

page_name = "edit_study"
edit=controllerEditStudy()

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
       
        <aside class="col bg-primary" >.col</aside>
      
      
        </div>
        </div>
        
        %s
    """ % (pageStart("Fields of Study", page_name, False), generateHeader(False), generateNav(page_name, False),edit,  pageEnd()))
