from controller.ctrl_cache import *
from controller.html_functions import *
from model.model_functions import getFieldsOfStudy
from cgi import FieldStorage, escape


def controllerEditStudy():
    # Edit the user's fields of study
    # Check if user is logged in, generate a form of the 4 main fields (radio), on submission generate a new form containing
    # the sub fields of said heading (checklist), on submit prevent user selecting all fields

    url = "edit_study.py"
    error_msg="<p></p>"

    result = loginToAccess(False)
    username = verifyLoggedIn(False)  # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print first checklist
        result=generateFieldHeadingsForm(url, error_msg)
        form_data=FieldStorage()

        if len(form_data)!=0:
            # Check which heading was selected and then generate the next form using the sub fields

            # Maybe do if main_field or fields of study - doesn't work
            # Maybe use a boolean to track if user submits on first form - won't work cuz of refresh
            # Maybe set the name in both forms to be the same, then depending on length of get list
            fields_of_study = form_data.getlist('fields_of_study')
            if len(fields_of_study)<6:
                # If the returned list is short, then the form must be main fields
                table_name="ask_%s" % fields_of_study[0]    # append fields_of_study to ask_ and get all fields from that table
                # Get all fields from table_name
                fields=getFieldsOfStudy(table_name)

                # Pass fields into a html_functions function and have it loop
                # through the dict adding a label and input each round
                result = generateStudyFieldsForm(url, fields, error_msg)
            else:
                # Else it must be one of the sub fields
                for x in fields_of_study:
                    result+='<p>%s</p>' % x

                #result=generateStudyFieldsForm(url, fields, error_msg)


            # Can't get form data twice, once you submit on the first form then it will loop back to top of file and start again



    return result
