#!/usr/local/bin/python3

from cgitb import enable
enable()

from controller.html_functions import *
from controller.ctrl_register import *

page_name = "register"
url= "register.py"


user_details, message_list = inputControllerRegistration()

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
                        <fieldset> <!-- Username, Email, Display Name, Password1, Password2 -->
                            <legend>Register</legend>
                            
                            <label for="txt_username">Username: </label>
                            <input type="text" name="txt_username" id="txt_username" value="%s" maxlength="20"/>
                            %s
                            <label for="txt_email">Email Address: </label>
                            <input type="text" name="txt_email" id="txt_email" value="%s" maxlength="50"/>
                            %s
                            <label for="txt_display_name">Display Name: </label>
                            <input type="text" name="txt_display_name" id="txt_display_name" value="%s" maxlength="35"/>
                            %s
                            <label for="txt_password1">Password: </label>
                            <input type="password" name="txt_password1" id="txt_password1" value="%s"/>
                            <label for="txt_password2">Re-Enter Password: </label>
                            <input type="password" name="txt_password2" id="txt_password2" value="%s"/>
                            %s
                            <input type="submit" value="Register"/>
                        </fieldset
                    </form>
                    %s
                  
                </main>
               
                %s
            </div>
        </div>

        %s
    """ % (pageStart("Register", page_name, False), generateHeader(False), generateNav(page_name, False), url, user_details[0], message_list[0], user_details[1], message_list[1], user_details[2], message_list[2], user_details[3], user_details[4], message_list[3], message_list[4], generateAsideRight(False), pageEnd()))
