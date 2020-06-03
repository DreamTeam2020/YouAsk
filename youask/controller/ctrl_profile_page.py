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
        """ % (profile_picture, details['username'], details['email'], details['reg_date'], details['score'], user_fields)


        logged=verifyLoggedIn('username', True)    # Returns username if logged in else 'UNVERIFIED'
        if logged!='UNVERIFIED':    # If logged in
            if logged == username:
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
                if check_connection == 'SEVER_ERROR':
                    server_error=True
                elif not check_connection:
                    # Display a way for the user to send a connect request
                    result += 'CONNECT WITH USER'
                else:
                    # Display a way for the user to disconnect
                    result += 'DISCONNECT FROM USER'

    return result

if __name__=='__main__':
    username='Cristian'
    result=controllerProfile(username)

    print(result)
