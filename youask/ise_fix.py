#!/usr/local/bin/python3

from cgitb import enable

enable()

page_name = "home"

print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en" id="%s">
        <head>
            <meta charset="utf-8" />
            <title>ISE TEST - YouAsk</title>
            <link rel="stylesheet" href="styles/styles.css" />
            <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
        </head>
        <body>
            <header>    <!-- A header section displayed at the top of the page--->
    
            </header>
    
            <main>      <!-- The main part of the website --->
                <h1>Does it work?</h1>
            </main>
    
            <aside>     <!-- A small aside that contains information not related to the main --->
    
            </aside>
        </body>
    </html>
    """)

