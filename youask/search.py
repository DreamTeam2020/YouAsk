#!/usr/local/bin/python3

from cgitb import enable
enable()
from controller.html_functions import *
from controller.ctrl_search import *

page_name = "search"
result, txt_search = searchKeyword()
url="search.py"
print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        %s
        
                <div class="container-fluid">
        <div class="row">
        <aside class="col-3 bg-primary" >.col</aside>
      
        <main class="col-6 bg-secondary" >   
       
                   <form action="%s" method="post">
                <fieldset>
                    <label for="txt_search">Search: </label>
                    <input type="text" name="txt_search" id="txt_search" value="%s"/>
                    
                    <input type="submit" value="Click to search"/>
                </fieldset>
            </form>
            %s
        
        </main>
       
        <aside class="col bg-primary" >.col</aside>
      
        </div>
        </div>
        %s
        %s
    """ % (pageStart("search", page_name, False), generateHeader(False), url, txt_search, result, generateNav(page_name, False), pageEnd()))
