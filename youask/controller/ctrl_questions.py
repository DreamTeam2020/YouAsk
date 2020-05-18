import os
from cgi import FieldStorage, escape

from model.model_functions import *
from controller.html_functions import shareLinks

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

    questions = getQuestion()
    converted_questions = convertDate(questions)

    form_data = FieldStorage()
    ordering = ""
    if len(form_data) != 0:
        ordering += escape(form_data.getfirst('chk_sorting', '').strip())

    ordered_questions = insertionSort(converted_questions, ordering)

    result = """
        <section>
    """

    for question in ordered_questions:
        result += """
                <section class="question">
                    <a href="question_pages/question_%s.py">
                        <p>%s</p>
        """ % (question['question_id'], question['question'])

        question_id = question['id']
        fields = getQuestionFields(question_id)  # Returns a fetchall of the fields used by the question
        if fields == 'EMPTY':
            fields_of_study = '<p class="error"><small>No Fields available</small></p>'
        else:
            fields_of_study = '<p><small>Fields of Study: '
            for row in fields:
                fields_of_study += '%s | ' % row['field']

            fields_of_study = fields_of_study[:-3]  # Remove the last 3 characters of the string
            fields_of_study += '</small></p>'

        share_links = shareLinks(False, question_id)

        result += """
                        %s
                        <p><small>Submitted By: %s | Score: %d | View Count: %d</small></p>
                    </a>
                    %s
                </section>
        """ % (fields_of_study, question['submitter'], question['score'], question['view_count'], share_links)

    result += """
        </section>
    """
    return result


