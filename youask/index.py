#!/usr/local/bin/python3

from cgitb import enable
enable()

from db_functions import pageStart, pageEnd

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            
        </header>
        
        <main>      <!-- The main part of the website --->
            <h1>test body</h1>
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
            
        </aside>
        
        <nav>       <!-- Includes the nav bar --->
            <ul>
                <li><a href="...">...</a></li>  
            </ul>
        </nav>
        %s
    """ % (pageStart("Home", "home"), pageEnd()))