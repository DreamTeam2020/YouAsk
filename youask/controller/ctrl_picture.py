from cgi import FieldStorage, escape

from model.model_functions import uploadpicture


def ctrlpicture():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('Upload', '').strip())
    if len(form_data) != 0:
        uploadpicture(form_data)
        return "success"
    else:
        return "false"