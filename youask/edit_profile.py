#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_edit_profile import *

page_name = "edit_profile"
edit=controllerEditProfile()

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
    """ % (pageStart("Edit Profile", page_name, False), generateHeader(False), generateNav(page_name, False),edit,  pageEnd()))
