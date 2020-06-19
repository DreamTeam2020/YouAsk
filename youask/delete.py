#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_delete import *

page_name = "delete"

result = controllerDelete()

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
    """ % (pageStart("Delete", page_name, False), generateHeader(False), generateNav(page_name, False), result,
           generateAsideRight(False), pageEnd()))



