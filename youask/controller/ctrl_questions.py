import os
from cgi import FieldStorage, escape

from model.model_functions import getQuestion

def conventdate(arr):
    for i in range(len(arr)):
        arr[i]["submission_date"]=arr[i]["submission_date"].strftime("%y")+ arr[i]["submission_date"].strftime("%m")+arr[i]["submission_date"].strftime("%d")+arr[i]["submission_date"].strftime("%H")+ arr[i]["submission_date"].strftime("%M")+arr[i]["submission_date"].strftime("%S")
        arr[i]["submission_date"]=int(arr[i]["submission_date"])
    return arr



def insertionSort(arr,text):
    for i in range(1, len(arr)):
        key = arr[i]["submission_date"]
        key1=arr[i]
        j = i - 1
        if(len(text)==5):
            while j >= 0 and key < arr[j]["submission_date"]:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key > arr[j]["submission_date"]:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1]["submission_date"] = key
        arr[j+1]=key1
    return arr



def controllerQuestions():
    facebooksrc = os.getcwd() + "/images/Facebook.png"
    twittersrc = os.getcwd() + "/images/Twitter.png"
    result = getQuestion()
    result=conventdate(result)
    form_data = FieldStorage()
    text=""
    if len(form_data) != 0:
        text  += escape(form_data.getfirst('cbox1', '').strip())
        text += escape(form_data.getfirst('cbox2', '').strip())
    result=insertionSort(result,text)
    questions = '<h1>question &nbsp submitter &nbsp score &nbsp view count &nbsp time &nbsp</h1>  '
    for x in result:
        SharetoFb = '&nbsp &nbsp &nbsp <a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;"> <img src=%s style="border:none 0;" alt="Share to Facebook" /></a> ' % (x, facebooksrc)
        SharetoTw = '&nbsp &nbsp &nbsp <a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~yc5/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja"><img src=%s style="border:none 0;" alt="Share to Twitter" /></a><p></p>' % (x, twittersrc)
        questions += '<section>%s &nbsp %s &nbsp %s &nbsp %s &nbsp %s %s %s</section> ' % (
            x["question"], x["submitter"], x["score"], x["view_count"], x["submission_date"],SharetoFb,SharetoTw)

    return questions


