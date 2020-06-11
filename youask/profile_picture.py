#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_picture import *

enable()

from controller.html_functions import *

page_name = "profile_picture"

print('Content-Type: text/html')
print()

result = controllerProfilePicture()

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
    """ % (pageStart("profile_picture", page_name, False), generateHeader(False), generateNav(page_name, False),result,  pageEnd()))
