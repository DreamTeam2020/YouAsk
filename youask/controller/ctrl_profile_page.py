from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_cache import *
from controller.ctrl_edit_profile import generateUserFields
from controller.ctrl_picture import getProfilePicture
from cgi import escape
from cgi import FieldStorage
from shutil import copyfile
import subprocess


def generateProfilePage(username):
    # Copy the profile template file, use sed to replace the username
    username=username.lower()
    new_file_name='profile_%s.py' % username
    copyfile('profile_pages/template_profile.py', 'profile_pages/%s' % new_file_name)

    subprocess.call(['sed', '-i', 's/820399/\'%s\'/g' % username, 'profile_pages/%s' % new_file_name])
    subprocess.call(['chmod', '705', 'profile_pages/%s' % new_file_name])

    return new_file_name


def controllerProfile(username):
    # Always: Profile picture, the data that is display when editing profile, Comment section maybe?
    # Logged In: Link to a connections list page, Link to user's submitted questions page, Link to edit profile
    # Logged In & not correct user: connect with link (or disconnect if already connected)

    server_error=False
    result = '<p> </p>'
    page_name = 'user_profile'

    # Get user's details
    details = getUserDetails(username)

    if details == 'SEVER_ERROR':
        server_error=True
    else:
        profile_picture = getProfilePicture(username, True)
        user_fields = generateUserFields(username)  # Generates the user fields section of edit profile
        result += """
        <article>
            %s
            <h1>%s</h1>
            <p>%s</p>
            <p><small>Member Since: %s | User Score: %d</small></p>
            
            %s
        <article>
        """ % (profile_picture, details['display_name'], details['email'], details['reg_date'], details['score'], user_fields)


        logged = verifyLoggedIn('username', True)    # Returns username if logged in else 'UNVERIFIED'
        if logged!='UNVERIFIED':    # If logged in
            SavePageToSession(page_name, True)  # Save the current page to the visitor's session store
            saveUserToSession(username, True)  # Save the username of this profile page to the visitor's session store
            if logged.lower() == username.lower():
                # If logged in and this is the user's profile, display links
                result += """
                    <section>
                        <p><a href='../connections.py'>Connections</a></p>
                        <p><a href='../users_questions.py'>Submitted Questions</a></p>
                        <p><a href='../edit_profile.py'>Edit Profile</a></p>
                    </section>
                """
            else:
                # If logged in and this is a different user from the profile page, display a connect button
                check_connection=checkConnectionWithUser(username, logged)

                if check_connection == 'SERVER_ERROR':
                    server_error=True
                elif not check_connection:
                    # Display a way for the user to send a connect request
                    result += '<p><a href="../connect.py">Connect With %s</a></p>' % details['display_name']
                else:
                    # Display a way for the user to disconnect
                    result += '<p><a href="../disconnect.py">Disconnect From %s</a></p>' % details['display_name']

    if server_error == True:
        result = '<p class="error">Server Error Has Occurred.</p>'

    return result

