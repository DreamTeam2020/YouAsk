#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_picture import *
from model.model_functions import getPictureCode

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

        <main>      <!-- The main part of the website --->
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("profile_picture", page_name, False), generateHeader(False), result, generateNav(page_name, False), pageEnd()))
