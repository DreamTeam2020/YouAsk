#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_search import *

page_name = "search"
result = searchkeyword()
url="search.py"
print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>Search your question</h1>
        </header>
        <main>      <!-- The main part of the website --->
          <form action="%s" method="post">
                
                  
                    
                    <label for="search">search: </label>
                    <input type="text" name="search" id="search"/>
                    
                    <input type="submit" value="Click to search"/>
            
            </form>
            %s
        </main>
        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>
        %s
        %s
    """ % (pageStart("search", page_name, False), url, result, generateNav(page_name, False), pageEnd()))
