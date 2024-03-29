from cgi import escape
from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import FieldStorage
from controller.ctrl_question_page import generateQuestionPage

def controllerSubmission():
    # Controller for the submit view, verify user input and then submit the question if verified

    url = "submit.py"
    question = ""
    description = ""
    coins = 0
    result = loginToAccess(False)
    error_msg = "<p> </p>"
    page_name = 'submit'

    session_table_key='question_submission_field_table'

    # Check if user is logged in
    # If logged in print form then do len form data
    username=verifyLoggedIn('username', False)   # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        # Present user with main fields, on submission generate question form with checklist below of sub fields

        savePageToSession(page_name, False)  # Save the current page to the visitor's session store

        result=generateFieldHeadingsForm(url, error_msg)
        form_data=FieldStorage()

        if len(form_data)!=0:
            # Check which heading was selected and then generate the next form using the sub fields

            if not form_data.getlist('fields_of_study'):
                # This will only occur on the sub checklist, the heading list will never be blank
                error_msg = '<p class="error">Please Select At Least One Field</p>'
                question = escape(form_data.getfirst('txt_question', '').strip())
                description = escape(form_data.getfirst('txt_description', '').strip())
                coins = escape(form_data.getfirst('num_coins', '').strip())
                coins = 0 if coins == '' else int(coins)

                table_name = getValueFromSession(session_table_key, False)
                fields = getFieldsOfStudy(table_name)  # Get all fields from table_name
                result = generateQuestionForm(url, question, description, coins, fields, error_msg)
                removeKeyFromSession(session_table_key, False)
            else:
                fields_of_study = form_data.getlist('fields_of_study')
                if fields_of_study[0] == 'humanities' or fields_of_study[0] == 'natural_sciences' or \
                        fields_of_study[0] == 'formal_sciences' or fields_of_study[0] == 'professions':
                    # If the data in fields_of_study is equal to one of the main fields
                    table_name = "ask_%s" % fields_of_study[0]  # Append fields_of_study to ask and get all fields from that table
                    fields = getFieldsOfStudy(table_name)  # Get all fields from table_name

                    # Get user's current fields from the table
                    saveToSession(session_table_key, table_name, False)  # Save table name to session for later use
                    result = generateQuestionForm(url, question, description, coins, fields, error_msg)
                else:
                    question = escape(form_data.getfirst('txt_question', '').strip())
                    description = escape(form_data.getfirst('txt_description', '').strip())
                    coins = escape(form_data.getfirst('num_coins', '').strip())
                    coins = 0 if coins == '' else int(coins)

                    user_coins = getCoins(username)
                    if not question:
                        error_msg = '<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
                    else:
                        if len(question) < 5:  # Remove this later for proper verification
                            error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity ' \
                                        'within the question. Profanity within the description will be filtered out.</p>'
                        elif user_coins < coins:
                            error_msg = '<p class="error">You Do Not Have Enough Coins</p>'
                        else:
                            # If input has been verified then insert the user's question in the database
                            submission_result = submitQuestion(username, question, description)  # Returns question id if success

                            if submission_result == "SERVER_ERROR":
                                error_msg = '<p class="error">Server Error Occurred</p>'
                            else:
                                # Add question fields to table
                                table=getValueFromSession(session_table_key, False)

                                sql_insert = """INSERT INTO ask_question_fields (question_id, area, field) VALUES """
                                for field in fields_of_study:
                                    # Remove the table name from the field, title will
                                    # capitalise first letter of each word. Replace underscores with spaces
                                    field = field.title().replace("_", " ")

                                    sql_insert += '("%s", "%s", "%s"),' % (submission_result, table, field)  # Append the question id, area and field onto the end of the query

                                sql_insert = sql_insert[:-1]  # Remove the last comma from the query
                                insert_result = executeInsertQuery(sql_insert)  # Insert into db
                                if insert_result == 'SERVER_ERROR':
                                    error_msg = '<p class="error">Server Error Occurred</p>'
                                else:
                                    # Question was submitted
                                    question = ''
                                    description = ''
                                    new_file = generateQuestionPage(submission_result)
                                    moveCoinsToQuestion(username, submission_result, coins)
                                    error_msg = '<p class="error">Question has been submitted, ' \
                                                'continue to question page <a href="question_pages/%s">here</a></p>' % new_file

                    table_name=getValueFromSession(session_table_key, False)
                    fields = getFieldsOfStudy(table_name)  # Get all fields from table_name
                    result = generateQuestionForm(url, question, description, coins, fields, error_msg)
                    removeKeyFromSession(session_table_key, False)

    return result
