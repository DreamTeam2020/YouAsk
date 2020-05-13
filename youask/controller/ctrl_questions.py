from model.model_functions import getQuestion

def conventdate(arr):
    for i in range(len(arr)):
        arr[i]["submission_date"]=arr[i]["submission_date"].strftime("%y")+ arr[i]["submission_date"].strftime("%m")+arr[i]["submission_date"].strftime("%d")+arr[i]["submission_date"].strftime("%H")+ arr[i]["submission_date"].strftime("%M")+arr[i]["submission_date"].strftime("%S")
        arr[i]["submission_date"]=int(arr[i]["submission_date"])
    return arr



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]["submission_date"]
        key1=arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]["submission_date"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1]["submission_date"] = key
        arr[j+1]=key1
    return arr



def controllerQuestions():
    result = getQuestion()
    result=conventdate(result)
    result=insertionSort(result)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp</h1>  '
    for x in result:
        SharetoFb = '<p><a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;">Share to facebook</a> </p>' % x
        SharetoTw = '<p><a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja">Share to Twitter</a></p>' % x
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s %s %s</section> ' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],SharetoFb,SharetoTw)

    return questions








'''
result = getQuestion()
result=conventdate(result)
result=insertionSort(result)
print(result)
'''