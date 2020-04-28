from model.model_functions import *

def generateQuestion(question):
    # Takes in a question from fetchall
    debug = "<h1>debug got into generate question</h1>"
    result_question = """
                        <section id="question">
                            <h1>%s</h1>
                            <p>%s</p>
                            <p><small>Submitted By: %s - Score: %d - View Count: %d</small></p>
                        </section>
        """ % (
    question['question'], question['submitter'], question['description'], question['score'], question['view_count'])

    return result_question, debug

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
    debug = "<h1>debug entered controller</h1>"
    server_error=False
    result_question = '<p> </p>'
    result_answers = '<p>This Question Hasn\'t Been Answered Yet.</p>'

    question = getQuestion(question_id)
    # From the answers table get all answers with questionID==question.id (If fetchall is empty )
    if question == "SERVER_ERROR":
        server_error=True
    '''
    else:
        debug = "<h1>debug Got the question now generating</h1>"
        result_question, debug = generateQuestion(question)

        # Get answers

        answers = getAnswers(question_id)
        if answers == "SERVER_ERROR":
            server_error=True
        elif answers != "EMPTY":
            debug = "<h1>debug getting the answers</h1>"
            result_answers = getAnswers(question_id)
    '''
    if server_error:
        result = '<p class="Error">Server Error Has Occurred</p>'
    else:
        result = result_question + result_answers
        debug = "<h1>Debug done, adding both and returning</h1>"

    return result, debug
