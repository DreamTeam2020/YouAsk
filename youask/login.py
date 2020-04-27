#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_login import *
from cgi import FieldStorage

page_name = "login"
url= "login.py"
user_email=""

error_msg="<p> </p>"

form_data = FieldStorage()

if len(form_data) !=0:
    logged_in, input_error, server_error, user_email, error_msg=inputControllerLogin(form_data)

    if logged_in==True:
        error_msg = '<p class="error">Successfully Logged In!</p>'
    if server_error==True:
        error_msg = '<p class="error">Server Error Occurred</p>'
    elif input_error==True:
        error_msg = '<p class="error">Invalid Username or Password</p>'

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>HEADER</h1>
        </header>

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
    """ % (pageStart("Login", page_name), url, user_email, error_msg, generateNav(page_name), pageEnd()))
