from controller.html_functions import *
from controller.ctrl_cache import *
from controller.ctrl_validation import displayNameValidation, passwordValidation
from model.model_functions import *
from cgi import FieldStorage, escape


def controllerEditProfile():
    # Edit user details, edit fields of study
    # Check if logged in, display the user's current details and a form where they can change them. On submission
    # validate the user input, do error messages then change details in db and session.

    url = "edit_profile.py"
    new_display_name=''
    old_password=''
    password1=''
    password2=''
    error_messages=['<p> </p>', '<p> </p>', '<p> </p>', '<p> </p>']  # Display name, current password, new password, error msg

    result = loginToAccess(False)
    username = verifyLoggedIn(False)   # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        # Display user's details and a form where they can be changed

        # Get user's details
        details=getUserDetails(username)
        if details == 'SEVER_ERROR':
            result='<p class="error">Server Error Occurred</p>'
        else:
            # Generate the form / the user doesnt have to fill the whole form in
            # ( i.e they just want to change display name not password )
            user_fields=generateUserFields(username)    # Generates the user fields section of edit profile

            result=generateEditDetailsForm(url, details, user_fields, new_display_name, old_password, password1, password2, error_messages)
            form_data=FieldStorage()
            if len(form_data)!=0:
                new_display_name= escape(form_data.getfirst('new_display_name', '').strip())
                old_password = escape(form_data.getfirst('old_password', '').strip())
                password1= escape(form_data.getfirst('password1', '').strip())
                password2 = escape(form_data.getfirst('password2', '').strip())

                display_result, password_result, error_messages=checkErrors(username, new_display_name, old_password, password1, password2)
                if display_result or password_result:
                    # If one was updated then get the user's new details and clear the user input
                    new_display_name='' if display_result else new_display_name
                    if password_result:
                        old_password, password1, password2='', '', ''

                    details=getUserDetails(username)
                result=generateEditDetailsForm(url, details, new_display_name, old_password, password1, password2, error_messages)

    return result


def checkErrors(username, new_display_name, old_password, password1, password2):
    # Check user input for errors
    display_updated=False
    password_updated=False
    error_messages=['<p> </p>', '<p> </p>', '<p> </p>', '<p> </p>']

    if (old_password and (not password1 or not password2)) or (password1 and (not old_password or not password2)) or (password2 and (not old_password or not password1)):
        error_messages[2]='<p class="error">If you are changing password, please fill in all password fields</p>'
    elif old_password and password1 and password2:
        # Check if old_password matches user's password
        match=checkOldPassword(username, old_password)
        if not match:
            error_messages[1]='<p class="error">Password does not match the user\'s password</p>'

        if password1!=password2:
            error_messages[2] = '<p class="error">New Passwords Must Match</p>'
        else:
            pass_result=passwordValidation(password1)
            if pass_result!='clear':
                error_messages[2]=pass_result
            else:
                # Update user's password & add success message to error_messages
                update_result_password = updateUserPassword(username, password1)
                if update_result_password == 'SERVER_ERROR':
                    error_messages[3] = '<p class="error">Server Error Occurred</p>'
                else:
                    error_messages[3] = '<p class="error">Password Successfully Updated</p>'
                    password_updated = True

    if new_display_name:
        # Validate the display name
        display_result=displayNameValidation(new_display_name)
        if display_result!='clear':
            error_messages[1]=display_result
        else:
            # Update user's display name in db and session & add success message to error_messages
            update_result_display=updateUserDisplayName(username, new_display_name)
            if update_result_display=='SERVER_ERROR':
                error_messages[3]='<p class="error">Server Error Occurred</p>'
            else:
                error_messages[1]='<p class="error">Display Name Successfully Updated</p>'
                display_updated=True

    return display_updated, password_updated, error_messages


def generateUserFields(username):
    # Display the user's selected fields under the 4 headings, returns a string of html
    field_data=["", "", "", ""]
    main_fields=['Humanities and Social Science', 'Natural Sciences', 'Formal Sciences', 'Professions and Applied Sciences']

    result='<section><p>Fields of Study: </p>'
    field_data[0] = getUserFieldsStudy(username, 'ask_humanities')  # Returns a fetchall of the user's fields under given main fields
    field_data[1] = getUserFieldsStudy(username, 'ask_natural_sciences')
    field_data[2] = getUserFieldsStudy(username, 'ask_formal_sciences')
    field_data[3] = getUserFieldsStudy(username, 'ask_professions')

    for i in range(len(main_fields)):
        result += '<p>%s: ' % main_fields[i]    # Field heading
        if field_data[i] == 'EMPTY':
            result += 'No Fields Selected</p>'
        else:
            for row in field_data[i]:
                result += '%s | ' % row['field']
            result = result[:-3]  # Remove the last 3 characters of the string

            result += '</p>'

    result += '</section>'

    return result

if __name__=='__main__':
    result=generateUserFields('whiskers')
    print(result)
