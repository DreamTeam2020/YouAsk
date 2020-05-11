from model.model_functions import getQuestion


def controllerQuestions():
    result = getQuestion()
    length = len(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp  '
    for x in result:
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s</section> <a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" style="margin-right:19px;">Share to facebook</a> ' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],x)

    return questions
