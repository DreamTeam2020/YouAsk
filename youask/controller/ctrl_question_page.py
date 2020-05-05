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
    # Takes in a question from fetchall
    result_question = """
                        <section class="question">
                            <h1>%s</h1>
                            <p>%s</p>
                            <p><small>Submitted By: %s - Score: %d - View Count: %d</small></p>
                        </section>
        """ % (question['question'], question['description'], question['submitter'],
               question['score'], question['view_count'])

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
    result_question = '<p> </p>'
    result_answers = '<p>This Question Hasn\'t Been Answered Yet.</p>'

    question = getSpecificQuestion(question_id)


    if question == "SERVER_ERROR":
        server_error=True
    else:
        result_question = generateQuestion(question)
        # Get answers
        answers = getAnswers(question_id)
        if answers == "SERVER_ERROR":
            server_error=True
        elif answers != "EMPTY":
            result_answers = generateAnswers(answers)

    if server_error:
        result = '<p class="Error">Server Error Has Occurred</p>'
    else:
        result = result_question + result_answers
        # Check if user is logged in, if so then allow them to answer

        logged=verifyLoggedIn(True)
        if logged!='UNVERIFIED':
            answer_form=controllerAnswerForm(logged, question_id)
            result+=answer_form
        else:
            result+=loginToAccess()
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
