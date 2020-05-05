#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *

page_name = "profile"

print('Content-Type: text/html')
print()

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
    """ % (pageStart("Profile", page_name, False), generateNav(page_name, False), pageEnd()))
