#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_register import *
from cgi import FieldStorage

page_name = "register"
redirect= "register.py"
user_details=["", "", ""]   # username, email, display_name

messageList=["<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>", "<p> </p>"]    # Contains error messages to be printed

form_data=FieldStorage()

if len(form_data) !=0:
    registered, server_error, user_details, messageList=inputControllerRegistration(form_data)

    if registered==True:
        messageList[4] = '<p class="error">Successfully Registered! <a href=login.py>Login Here</a></p>'
        redirect = 'registered.py' #Redirect to a different page after registration here
    elif server_error == True:
        messageList[4] = '<p class="error">Server Error Occurred</p>'
    else:
        messageList=messageList


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
                <fieldset> <!-- Username, Email, Display Name, Password1, Password2 -->
                    <legend>Register</legend>
                    
                    <label for="username">Username: </label>
                    <input type="text" name="username" id="username" value="%s" maxlength="20"/>
                    %s
                    <label for="email">Email Address: </label>
                    <input type="text" name="email" id="email" value="%s" maxlength="50"/>
                    %s
                    <label for="display_name">Display Name: </label>
                    <input type="text" name="display_name" id="display_name" value="%s" maxlength="35"/>
                    %s
                    <label for="password1">Password: </label>
                    <input type="password" name="password1" id="password1"/>
                    <label for="password2">Re-Enter Password: </label>
                    <input type="password" name="password2" id="password2"/>
                    %s
                    <input type="submit" value="Register"/>
                </fieldset
            </form>
            %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->
        </aside>

        %s
        %s
    """ % (pageStart("Register", page_name), redirect, user_details[0], messageList[0], user_details[1], messageList[1], user_details[2], messageList[2], messageList[3], messageList[4], generateNav(page_name), pageEnd()))
