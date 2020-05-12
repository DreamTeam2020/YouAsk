from model.model_functions import getQuestion




def controllerQuestions():
    result = getQuestion()
    insertionSort(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp</h1>  '
    for x in result:
        SharetoFb = '<h5><a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;">Share to facebook</a> </h5>' % x
        SharetoTw = '<h5><a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja">Share to Twitter</a></h5>' % x
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s </section> %s %s' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],SharetoFb,SharetoTw)

    return questions




def dateconvert(s):
   news=""
   for x in range(len(s)):
       if 47 < ord(s[x]) < 58:
           news+=s[x]
           print(ord(s[x]))
       else: print(ord(s[x]))

   return int(news)


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = dateconvert(arr[i]["submission_date"])

        j = i - 1
        while j >= 0 and key < dateconvert(arr[j]["submission_date"]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1]["submission_date"] = key