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
    result = loginToAccess(False)
    error_msg = "<p> </p>"

    # Check if user is logged in
    # If logged in print form then do len form data
    username=verifyLoggedIn(False)   # Returns username if logged in, else UNVERIFIED

    if username != 'UNVERIFIED':  # If the user is logged in, print the question submission form
        # Present user with main fields, on submission generate question form with checklist below of sub fields

        result=generateFieldHeadingsForm(url, error_msg)
        form_data=FieldStorage()

        if len(form_data)!=0:
            # Check which heading was selected and then generate the next form using the sub fields

            fields_of_study = form_data.getlist('fields_of_study')
            if fields_of_study[0] == 'humanities' or fields_of_study[0] == 'natural_sciences' or \
                            fields_of_study[0] == 'formal_sciences' or fields_of_study[0] == 'professions':
                # If the data in fields_of_study is equal to one of the main fields
                table_name = "ask_%s" % fields_of_study[0]  # Append fields_of_study to ask and get all fields from that table
                fields = getFieldsOfStudy(table_name)  # Get all fields from table_name

                # Get user's current fields from the table

                result = generateQuestionForm(url, question, description, fields, error_msg)
            else:
                '''
                separator = '~'  # This will define the value used to split the table name from the field name
                table = fields_of_study[0].split(separator, 1)[-1]
                
                question = escape(form_data.getfirst('question', '').strip())
                description = escape(form_data.getfirst('description', '').strip())

                if not question:
                    error_msg = '<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
                else:
                    # Filter out profanity on description, block questions that include profanity
                    if len(question) < 5:  # Remove this later for proper verification
                        error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity ' \
                                    'within the question. Profanity within the description will be filtered out.</p>'
                    else:
                        # If input has been verified then insert the user's question in the database
                        submission_result = submitQuestion(username, question, description)
                        if submission_result == "SERVER_ERROR":
                            error_msg = '<p class="error">Server Error Occurred</p>'
                        else:
                            # Question was submitted
                            question = ''
                            description = ''
                            new_file = generateQuestionPage(submission_result)
                            error_msg = '<p class="error">Question has been submitted, ' \
                                        'continue to question page <a href="question_pages/%s">here</a></p>' % new_file

                result = generateQuestionForm(url, question, description, error_msg)
                '''
                result='<h1>test</h1>'




        '''
        result = generateQuestionForm(url, question, description, error_msg)

        form_data=FieldStorage()

        if len(form_data)!=0:
            question= escape(form_data.getfirst('question', '').strip())
            description = escape(form_data.getfirst('description', '').strip())

            if not question:
                error_msg='<p class="error">Question Field Must Be Filled</p>'  # If no question is entered
            else:
                # Filter out profanity on description, block questions that include profanity
                if len(question) < 5:    # Remove this later for proper verification
                    error_msg = '<p class="error">Invalid question, please <em>Do Not</em> include profanity ' \
                                'within the question. Profanity within the description will be filtered out.</p>'
                else:
                    # If input has been verified then insert the user's question in the database
                    submission_result = submitQuestion(username, question, description)
                    if submission_result=="SERVER_ERROR":
                        error_msg = '<p class="error">Server Error Occurred</p>'
                    else:
                        #Question was submitted
                        question=''
                        description=''
                        new_file=generateQuestionPage(submission_result)
                        error_msg = '<p class="error">Question has been submitted, ' \
                                    'continue to question page <a href="question_pages/%s">here</a></p>' % new_file

            result = generateQuestionForm(url, question, description, error_msg)
        '''
    return result
