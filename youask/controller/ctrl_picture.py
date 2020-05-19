import base64
import cgi
import os
from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn
from model.model_functions import upLoadPicture, upLoadFromLocal, getPictureCode

def ctrlPicture():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('Upload', '').strip())
    if len(form_data) != 0:
        upLoadPicture(form_data)
        return "success"
    else:
        return "false"


def generateForm():
    result = verifyLoggedIn('username', False)
    if result == 'UNVERIFIED':
        return result+" please log in first "
    else:
        result= ' <form action="profile_picture.py" enctype="multipart/form-data" method="post">'\
                  '<fieldset> <!--  Description -->' \
                 '<input type="file" id="file" name="myfile"><br><br>'  \
                  '<input type="submit" value="Submit Picture"/>'  \
               '</fieldset>' \
            '</form>'
    return result
    


def ctrlSubmitPic():

    form = cgi.FieldStorage()
    result = verifyLoggedIn('username', False)

    if (len(form) != 0):

            fileitem = form['myfile']
            if fileitem.filename:
                encoded_string = base64.b64encode(fileitem.file.read())
                upLoadFromLocal(result, encoded_string)
                return 'success please refresh to get your latest profile picture'
    return ''


def getProfilePicture(sub_dir):
    # Get the username, get the profile picture from the
    # database, if none there then display blank image else display profile picture

    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    username = verifyLoggedIn('username', False)

    picture_code = getPictureCode(username)
    profile_picture='%simages/unavailable.png' % prefix

    if picture_code == 'EMPTY':
        result = """
            <figure>
                <img src="%s" title="Blank Profile Picture" alt="A simplistic blank profile picture, depicting a simple grey circle above a grey half ellipse which resembles a person."/>
                <figcaption>
                    <small>
                        (<a href="https://creativecommons.org/share-your-work/public-domain/cc0/">Licensed Under CC0</a>)
                    </small>
                </figcaption>
            </figure>
        """ % profile_picture
    elif picture_code == 'SERVER_ERROR':
        result = '<p class="error">Server Error Occurred</p>'
    else:
        result = """
            <figure>
                <img src="data:image/png;base64, %s" title="User's Profile Picture" alt="This image was uploaded by the user, therefore there is no description available."/>
            </figure>
        """ % picture_code

    return result
