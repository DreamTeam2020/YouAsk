#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_picture import ctrlpicture
from model.model_functions import getpicturecode

enable()

from controller.html_functions import *

page_name = "profile_picture"


print('Content-Type: text/html')
print()
picsrc=getpicturecode()
result=ctrlpicture()


print("""
    %s
    <body>
        %s

        <main>      <!-- The main part of the website --->
         
            <div>
  
  <img src="data:image/png;base64, %s" alt="Red dot" />
</div>
%s   it is a log    %s

  <form action="profile_picture.py" method="post">
                
                  
                    
                    <label for="Upload a pic ">Upload Pic:  please type the pic's name (which is in images folder)</label>
                    <input type="text" name="Upload" id="Upload"/>
                    
                    <input type="submit" value="Click to upload"/>
            
            </form>

        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("profile_picture", page_name, False), generateHeader(False), picsrc, result, getpicturecode(), generateNav(page_name, False), pageEnd()))
