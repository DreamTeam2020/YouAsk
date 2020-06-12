from controller.ctrl_cache import *
from controller.html_functions import *
from model.model_functions import *
from cgi import FieldStorage, escape


def controllerEditStudy():
    # Edit the user's fields of study
    # Check if user is logged in, generate a form of the 4 main fields (radio), on submission generate a new form containing
    # the sub fields of said heading (checklist), on submit prevent user selecting all fields

    url = "edit_study.py"
    page_name = 'edit_study'
    error_msg="<p>Go back to edit profile <a href='edit_profile.py>here</a></p>"

    session_table_key='question_submission_field_table'

    result = loginToAccess(False)
    username = verifyLoggedIn('username', False)  # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print first checklist

        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        result=generateFieldHeadingsForm(url, error_msg)
        form_data=FieldStorage()

        if len(form_data)!=0:
            # Check which heading was selected and then generate the next form using the sub fields

            fields_of_study = form_data.getlist('fields_of_study')

            if fields_of_study[0] == 'humanities' or fields_of_study[0] == 'natural_sciences' or \
                    fields_of_study[0] == 'formal_sciences' or fields_of_study[0]=='professions':
                # If the data in fields_of_study is equal to one of the main fields

                table_name = "ask_%s" % fields_of_study[0]    # Append fields_of_study to ask and get all fields from that table
                fields = getFieldsOfStudy(table_name)   # Get all fields from table_name

                # Get user's current fields from the table
                user_fields=getUserFieldsStudy(username, table_name)

                # Pass fields into a html_functions function and have it loop
                # through the dict adding a label and input each round.
                saveToSession(session_table_key, table_name, False)    # Save table name to session for later use
                result = generateStudyFieldsForm(url, fields, user_fields, error_msg)
            else:
                # Else form must be one of the sub fields
                # Insert the data into the table ( Try to avoid 1 by 1 insertion )
                # ( Sql statement equals and do += in each loop to add field and username pair to end of insert statement )
                # ( How to get the table name? ) -- Append a value to the end of each value/id in the form to signify which table to use

                table = getValueFromSession(session_table_key, False)

                sql_insert = """INSERT INTO %s (field, username) VALUES """ % table
                for field in fields_of_study:
                    # Remove the table name from the field, title will
                    # capitalise first letter of each word. Replace underscores with spaces
                    field = field.title().replace("_", " ")

                    sql_insert += '("%s", "%s"),' % (field, username)   # Append the field and username onto the end of the query

                sql_insert = sql_insert[:-1]    # Remove the last comma from the query
                removal_result=removeFieldsOfStudy(username, table)     # Remove the old data from table to allow user to remove fields
                insert_result=executeInsertQuery(sql_insert)    # Insert into db
                if insert_result == 'SERVER_ERROR' or removal_result=='SERVER_ERROR':
                    error_msg += '<p class="error">Server Error Occurred</p>'
                else:
                    error_msg += '<p class="error">Successfully Updated</p>'

                fields = getFieldsOfStudy(table)   # Get all fields from table_name
                user_fields=getUserFieldsStudy(username, table)
                result = generateStudyFieldsForm(url, fields, user_fields, error_msg)
    return result
