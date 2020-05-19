import base64
import cgi
import os
from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn
from model.model_functions import uploadProfilePicture, getPictureCode
from controller.html_functions import loginToAccess


def controllerProfilePicture():
    username = verifyLoggedIn('username', False)
    result = loginToAccess(False)

    if username != 'UNVERIFIED':
        profile_picture = getProfilePicture(username, False)
        form_generate = generateForm()
        submission = submitProfilePicture(username)

        result = profile_picture + form_generate + submission

    return result


def generateForm():
    result = """
        <form action="profile_picture.py" enctype="multipart/form-data" method="post">
            <fieldset> <!--  Description -->
                <input type="file" id="file" name="myfile"><br><br>
                <input type="submit" value="Submit Picture"/>
            </fieldset>
        </form>"""

    return result
    

def submitProfilePicture(username):
    form_data = FieldStorage()
    result = ''

    if len(form_data) != 0:
        file_item = form_data['myfile']
        if file_item.filename:
            encoded_string = base64.b64encode(file_item.file.read())
            submission = uploadProfilePicture(username, encoded_string)
            if submission == 'SERVER_ERROR':
                result = '<p class="error">Server Error Occurred</p>'
            else:
                result = '<p class="error">Profile picture was updated, please refresh to see latest change.</p>'
    return result


def getProfilePicture(username, sub_dir):
    # Get the username, get the profile picture from the
    # database, if none there then display blank image else display profile picture

    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

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
