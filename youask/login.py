#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_login import *

page_name = "login"
url= "login.py"

user_email, error_msg=inputControllerLogin()

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        %s

        <main>      <!-- The main part of the website --->
            <form action="%s" method="post">
                <fieldset> <!-- Username or Email, Password -->
                    <legend>Log In</legend>

                    <label for="user_email">Username or Email: </label>
                    <input type="text" name="user_email" id="user_email" value="%s" maxlength="50"/>
                    
                    <label for="password">Password: </label>
                    <input type="password" name="password" id="password"/>
                    
                    <input type="submit" value="Log In"/>
                </fieldset
            </form>
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Login", page_name, False), generateHeader(False), url, user_email, error_msg, generateNav(page_name, False), pageEnd()))
