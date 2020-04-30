from model.model_functions import *
from controller.html_functions import *
from controller.ctrl_cache import *
from cgi import escape
from cgi import FieldStorage

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
        debug="<p>%s</p>" % logged
        if logged!='UNVERIFIED':
            #answer_form=controllerAnswerForm(logged, question_id)
            answer_form='<h1>logged in</h1>'
            result+=answer_form
        else:
            #debug="<p>%s</p>" % logged
            result+="<h1>NOT LOGGED IN YAHOOO</h1>"
        result+=debug
    return result

def controllerAnswerForm(username, question_id):
    # Generate form here, then do len form data, then generate form again for the error messages
    answer = ''
    error_msg = '<p> </p>'
    page_url = 'question_template.py'  # page_url='%d.py' % question_id

    answer_form = generateAnswerForm(page_url, answer, error_msg)
    form_data = FieldStorage

    if len(form_data)!=0:
        server_error = False
        input_error = False
        submitted = False

        answer = escape(form_data.getfirst('answer', '').strip())
        if not answer:
            error_msg = '<p class="error">Answer Field Must Be Filled</p>'  # If no answer is entered
        else:
            # Filter out profanity on the answer here
            if len(answer) < 4:  # Remove this later for proper verification
                input_error = True
            else:
                # If input has been verified then insert the user's answer in the database
                submission_result = submitAnswer(username, answer, question_id)
                if submission_result == "SERVER_ERROR":
                    server_error = True
                else:
                    submitted = True

        if submitted:
            error_msg = '<p class="error">Question Has Been Submitted</p>'
            # Provide link to the question page
        elif server_error:
            error_msg = '<p class="error">Server Error Occurred</p>'
        elif input_error:
            error_msg = '<p class="error">Invalid answer, please <em>Do Not</em> include profanity within the question. profanity within the description will be filtered out</p>'

        answer_form = generateAnswerForm(page_url, answer, error_msg)

    return answer_form

if __name__=="__main__":
    # It works
    results=controllerQuestionAnswers(3)
    print(results)
