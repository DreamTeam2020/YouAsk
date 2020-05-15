from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import escape
from cgi import FieldStorage
from shutil import copyfile
import subprocess

def generateQuestionPage(question_id):
    # Copy the question template file, use sed to replace the question id
    new_file_name='question_%d.py' % question_id
    copyfile('question_pages/template_question.py', 'question_pages/%s' % new_file_name)

    # sed -i 's/820399/%d/g' % question_id
    subprocess.call(['sed', '-i', 's/820399/%d/g' % question_id, 'question_pages/%s' % new_file_name])
    # chmod 705 question_pages/question_*
    subprocess.call(['chmod', '705', 'question_pages/%s' % new_file_name])

    return new_file_name

def generateQuestion(question):
    # Takes in a question from fetchall and generate the question display (will also generate the question's fields)
    result_question = """
                    <section class="question">
                        <h1>%s</h1>
                        <p>%s</p>
        """ % (question['question'], question['description'])

    question_id=question['id']
    fields=getQuestionFields(question_id)   #Returns a fetchall of the fields used by the question
    if fields=='EMPTY':
        fields_of_study='<p class="error">No Fields available</p>'
    else:
        fields_of_study='<p>Fields of Study: '
        for row in fields:
            fields_of_study+='%s | ' % row['field']

        fields_of_study=fields_of_study[:-3]    # Remove the last 3 characters of the string

    facebook_src = "../images/Facebook.png"
    twitter_src = "../images/Twitter.png"
    share_to_fb = '<a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~cgg1/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;"> <img src=%s style="border:none 0;" alt="Share to Facebook" /></a>' % (question_id, facebook_src)
    share_to_tw = '<a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~cgg1/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja"><img src=%s style="border:none 0;" alt="Share to Twitter" /></a>' % (question_id, twitter_src)

    result_question+="""
                        %s
                        <p><small>Submitted By: %s | Score: %d | View Count: %d</small></p>
                        %s %s
                        
                    </section>
    """ % (fields_of_study, question['submitter'], question['score'], question['view_count'], share_to_fb, share_to_tw)

    return result_question

def generateAnswers(answers):
    result_answers = '<section id="answers_list">'

    for row in answers:
        result_answers += """
                                <section class="answer">
                                    <p>%s</p>
                                    <p><small>Submitted By: %s - Score: %d</small></p>
                                </section>
                """ % (row['answer'], row['submitter'], row['score'])
    result_answers += '</section>'

    return result_answers

def controllerQuestionAnswers(question_id):
    server_error=False
    result='<p> </p>'
    result_question = '<p> </p>'
    result_answers = '<p>This Question Hasn\'t Been Answered Yet.</p>'

    question = getSpecificQuestion(question_id)

    if question == "SERVER_ERROR":
        server_error=True
    else:
        result_question = generateQuestion(question)

    if not server_error:
        result = result_question
        submitter=question['submitter']

        # Check if user is logged in, if so then allow them to answer
        logged=verifyLoggedIn('username', True)    # Returns username if logged in else 'UNVERIFIED'
        if logged!='UNVERIFIED': # If logged in
            # If the user is the submitter of the question (else if the user has the correct fields to answer)

            question_fields = getQuestionFields(question_id)

            if logged == submitter:
                answer_form=controllerAnswerForm(logged, question_id)
                result += answer_form
            elif question_fields!='EMPTY' and question_fields!='SERVER_ERROR':
                # Get the user's fields of study from the table that contains the questions fields
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
            else:
                # The query was either empty of a server error occurred
                result += '<section><p class="error">Server Error Has Occurred.</p></section>'
        else:
            result+=loginToAccess(True)

        # Get answers
        answers = getAnswers(question_id)
        if answers == "SERVER_ERROR":
            server_error=True
        elif answers != "EMPTY":
            result_answers = generateAnswers(answers)

        result+=result_answers

    if server_error:
        result = '<p class="error">Server Error Has Occurred</p>'

    return result

def controllerAnswerForm(username, question_id):
    # Generate form here, then do len form data, then generate form again for the error messages
    answer = ''
    error_msg = '<p> </p>'
    page_url='question_%d.py' % question_id

    answer_form = generateAnswerForm(page_url, answer, error_msg)
    form_data = FieldStorage()

    if len(form_data)!=0:
        server_error = False
        input_error = False

        answer = escape(form_data.getfirst('answer', '').strip())
        if not answer:
            error_msg = '<p class="error">Answer Field Must Be Filled</p>'  # If no answer is entered
        else:
            # Filter out profanity on the answer here
            if len(answer) < 3:  # Remove this later for proper verification
                input_error = True
            else:
                # If input has been verified then insert the user's answer in the database
                submission_result = submitAnswer(username, answer, question_id)
                if submission_result == "SERVER_ERROR":
                    server_error = True
                else:
                    error_msg = '<p class="error">Answer Has Been Submitted</p>'
                    answer=''

        if server_error:
            error_msg = '<p class="error">Server Error Occurred</p>'
        elif input_error:
            error_msg = '<p class="error">Invalid answer, please ensure the answer is more than 3 characters, profanity within the answer will be filtered out</p>'

        answer_form = generateAnswerForm(page_url, answer, error_msg)

    return answer_form

if __name__=="__main__":
    # It works
    results=controllerQuestionAnswers(3)
    print(results)
