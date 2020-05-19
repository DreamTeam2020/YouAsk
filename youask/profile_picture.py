#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_picture import *
from model.model_functions import getPictureCode

enable()

from controller.html_functions import *

page_name = "profile_picture"

print('Content-Type: text/html')
print()
profile_picture = getProfilePicture(False)
form_generate = generateForm()
result = ctrlSubmitPic()

print("""
    %s
    <body>
        %s

        <main>      <!-- The main part of the website --->
            %s

      %s
             %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("profile_picture", page_name, False), generateHeader(False), profile_picture, form_generate, result,
           generateNav(page_name, False), pageEnd()))
