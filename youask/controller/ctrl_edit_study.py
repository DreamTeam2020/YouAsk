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
            #Check which heading was selected and then generate the next form using the sub fields

            main_field= form_data.getfirst('main_fields', '')
            result="<p>%s</p>" % main_field
            # if i can just get data from the form under main_fields and it returns an id, then append to ask_ and get all fields from that table

            #table_name="ask_%s" % main_field
            #get all fields from table_name
            #fields=getFieldsOfStudy(table_name)

    return result
