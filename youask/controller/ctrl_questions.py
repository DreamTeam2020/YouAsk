import os
from cgi import FieldStorage, escape

from model.model_functions import *
from controller.html_functions import generateQuestionsDisplay
from controller.ctrl_cache import verifyLoggedIn, savePageToSession

def convertDate(questions):
    for i in range(len(questions)):
        questions[i]["submission_date"] = questions[i]["submission_date"].strftime("%y") + questions[i]["submission_date"].strftime("%m")+questions[i]["submission_date"].strftime("%d")+questions[i]["submission_date"].strftime("%H")+ questions[i]["submission_date"].strftime("%M")+questions[i]["submission_date"].strftime("%S")
        questions[i]["submission_date"] = int(questions[i]["submission_date"])

    return questions


def insertionSort(arr, sorting):
    for i in range(1, len(arr)):
        key = arr[i]["submission_date"]
        key1 = arr[i]
        j = i - 1
        if sorting == "chk_latest":
            while j >= 0 and key < arr[j]["submission_date"]:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key > arr[j]["submission_date"]:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1]["submission_date"] = key
        arr[j+1] = key1
    return arr


def controllerQuestions():
    page_name = 'questions'
    verify_logged = verifyLoggedIn('username', False)

    if verify_logged != 'UNVERIFIED':
        savePageToSession(page_name, True)  # Save the current page to the visitor's session store

    questions = getQuestion()
    converted_questions = convertDate(questions)

    form_data = FieldStorage()
    ordering = ""
    if len(form_data) != 0:
        ordering += escape(form_data.getfirst('chk_sorting', '').strip())

    ordered_questions = insertionSort(converted_questions, ordering)

    result = generateQuestionsDisplay(ordered_questions, False)

    return result


