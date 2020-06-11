#!/usr/local/bin/python3

from cgitb import enable
enable()
import sys
sys.path.append("../")  # Because it's a subdirectory we append this to all of the subsequent imports

from controller.ctrl_profile_page import *
from controller.html_functions import *

page_name='user_profile'
result = controllerProfile(820399)


# Add a form to the end so users can answer the question posed


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
    """ % (pageStart("User Profile", page_name, True), generateHeader(True), generateNav(page_name, True), result, pageEnd()))
