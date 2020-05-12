from model.model_functions import getQuestion


def controllerQuestions():
    result = getQuestion()
    length = len(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp</h1>  '
    for x in result:
        SharetoFb = '<h5><a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;">Share to facebook</a> </h5>' % x
        SharetoTw = ' <a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja">Share to Twitter</a>' % x
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s </section> %s %s' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],SharetoFb,SharetoTw)

    return questions




