#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_login import *

page_name = "login"
url= "login.py"

user_email, password, error_msg = inputControllerLogin()

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        %s
        %s
        
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>
              
                <main class="col-6 bg-secondary" >   
           
                    <form action="%s" method="post">
                        <fieldset> <!-- Username or Email, Password -->
                            <legend>Log In</legend>
        
                            <label for="txt_user_email">Username or Email: </label>
                            <input type="text" name="txt_user_email" id="txt_user_email" value="%s" maxlength="50"/>
                            
                            <label for="txt_password">Password: </label>
                            <input type="password" name="txt_password" id="txt_password" value="%s"/>
                            
                            <input type="submit" value="Log In"/>
                        </fieldset
                    </form>
                    %s
                 
                </main>
               
                <aside class="col bg-primary" >.col</aside>
          
            </div>
        </div>

        
        %s
    """ % (pageStart("Login", page_name, False), generateHeader(False), generateNav(page_name, False),url, user_email, password, error_msg,  pageEnd()))
