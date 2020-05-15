
from controller.html_functions import *
from model.model_functions import *
from controller.ctrl_question_page import *

url = "submit.py"
table = 'ask_question_fields'
username='PatrickPeters'
error_msg = "<p> </p>"

question = "First I limp to the side"
description = "Like my legs was broken"
fields_of_study=['human_physical_performance_and_recreation', 'law']

if not question:
    error_msg = '<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
else:
    if len(fields_of_study) == 0:
        # If this passes then there must be no fields selected
        error_msg = '<p class="error">Please Select At Least One Field</p>'
    else:
        if len(question) < 5:  # Remove this later for proper verification
            error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity ' \
                        'within the question. Profanity within the description will be filtered out.</p>'
        else:

            # If input has been verified then insert the user's question in the database
            submission_result = submitQuestion(username, question, description)  # Returns question id if success

            if submission_result == "SERVER_ERROR":
                error_msg = '<p class="error">Server Error Occurred</p>'
            else:
                # Add question fields to table
                #table = getValueFromSession(session_table_key, False)

                sql_insert = """INSERT INTO ask_question_fields (question_id, area, field) VALUES """
                for field in fields_of_study:
                    # Remove the table name from the field, title will
                    # capitalise first letter of each word. Replace underscores with spaces
                    field = field.title().replace("_", " ")

                    sql_insert += '("%s", "%s", "%s"),' % (
                    submission_result, table, field)  # Append the question id, area and field onto the end of the query

                sql_insert = sql_insert[:-1]  # Remove the last comma from the query
                insert_result = executeInsertQuery(sql_insert)  # Insert into db
                if insert_result == 'SERVER_ERROR':
                    error_msg = '<p class="error">Server Error Occurred</p>'
                else:
                    # Question was submitted
                    question = ''
                    description = ''
                    #error_msg='success'
                    new_file = generateQuestionPage(submission_result)
                    error_msg = '<p class="error">Question has been submitted, continue to question page <a href="question_pages/%s">here</a></p>' % new_file

#table_name = getValueFromSession(session_table_key, False)
table_name=table
fields = getFieldsOfStudy(table_name)  # Get all fields from table_name
result = generateQuestionForm(url, question, description, fields, error_msg)
#removeKeyFromSession(session_table_key, False)

print(result)
"""

# Get the user's fields of study from the table that contains the questions fields
result=""
question_id=49
question_fields = getQuestionFields(question_id)
logged='PatrickPeters'
authorised=False
user_fields=getUserFieldsStudy(logged, question_fields[0]['area'])

if user_fields!='EMPTY' and user_fields!='SERVER_ERROR':
    for row in question_fields:
        for user_row in user_fields:
            if row['field'] == user_row['field']:
                authorised = True
                break
        if authorised:
            break

if authorised:
    # The user has at least one field the same as the question
    answer_form=controllerAnswerForm(logged, question_id)
    result+=answer_form
else:
    # The user is not the submitter and does not have the correct fields
    result += '<section><p class="error">To answer this question you must be in the same field of study or be the original submitter of the question. You can edit your fields on your profile page <a href="../profile.py">here</a>.</p></section>'

print(result)
"""