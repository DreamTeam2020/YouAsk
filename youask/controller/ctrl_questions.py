from model.model_functions import getQuestion
import datetime




def controllerQuestions():
    result = getQuestion()
    result=insertionSort(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp</h1>  '
    for x in result:
        SharetoFb = '<h5><a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;">Share to facebook</a> </h5>' % x
        SharetoTw = '<h5><a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja">Share to Twitter</a></h5>' % x
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s </section> %s %s' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],SharetoFb,SharetoTw)

    return questions




def dateconvert(s):
   news=""
   for x in range(19):
       if 48 <= ord(s[x]) <= 57:
           news+=s[x]



   return (news)


def conventdate(arr):
    for i in range(len(arr)):
        print(i+1)
        arr[i]["submission_date"]=arr[i]["submission_date"].strftime("%y")+ arr[i]["submission_date"].strftime("%m")+arr[i]["submission_date"].strftime("%d")+arr[i]["submission_date"].strftime("%H")+ arr[i]["submission_date"].strftime("%M")+arr[i]["submission_date"].strftime("%S")
        arr[i]["submission_date"]=int(arr[i]["submission_date"])
    return arr



def insertionSort(arr):
    for i in range(1, len(arr)):
        key =arr[i]["submission_date"]
        j = i - 1
        while j >= 0 and key > arr[j]["submission_date"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1]["submission_date"] = key
    return arr



