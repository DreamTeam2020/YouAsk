from model.model_functions import getQuestion


def controllerQuestions():
    result = getQuestion()
    length = len(result)
    questions = ''
    for x in result:
        questions += '<p>%s</p>' % x
    return questions
