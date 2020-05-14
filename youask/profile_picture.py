#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_picture import ctrlPicture, ctrlSubmitPic
from model.model_functions import getPictureCode

enable()

from controller.html_functions import *

page_name = "profile_picture"


print('Content-Type: text/html')
print()
picsrc=getPictureCode()
result=ctrlSubmitPic()



print("""
    %s
    <body>
        %s

        <main>      <!-- The main part of the website --->
         
            <div>
  
  <img src="data:image/png;base64, %s" alt="Red dot" />
</div>

            
             <form action="profile_picture.py" method="post">
            <fieldset> <!--  Description -->
                
               <input type="file" id="myfile" name="myfile"><br><br>
                <input type="submit" value="Submit Picture"/>
            </fieldset
        </form>
         %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("profile_picture", page_name, False), generateHeader(False), picsrc, result,generateNav(page_name, False), pageEnd()))
