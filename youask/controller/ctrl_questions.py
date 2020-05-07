from model.model_functions import getQuestion


def controllerQuestions():
    result = getQuestion()
    length = len(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp '
    for x in result:
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s</section>' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"])

    return questions
