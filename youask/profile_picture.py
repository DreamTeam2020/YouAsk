#!/usr/local/bin/python3

from cgitb import enable

from model.model_functions import picture

enable()

from controller.html_functions import *

page_name = "profile_picture"


print('Content-Type: text/html')
print()
picture()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->

        </header>

        <main>      <!-- The main part of the website --->
            <h1>test page</h1>
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("profile_picture", page_name, False), generateNav(page_name, False), pageEnd()))
