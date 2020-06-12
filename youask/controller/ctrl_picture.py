import base64
from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn, savePageToSession
from model.model_functions import uploadProfilePicture
from controller.html_functions import loginToAccess, getProfilePicture


def controllerProfilePicture():
    page_name = 'profile_picture'
    username = verifyLoggedIn('username', False)
    result = loginToAccess(False)

    if username != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store
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



