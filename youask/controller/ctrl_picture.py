import base64
from cgi import FieldStorage, escape

from model.model_functions import upLoadPicture, upLoadFromLocal


def ctrlPicture():
    form_data = FieldStorage()
    form_data = escape(form_data.getfirst('Upload', '').strip())
    if len(form_data) != 0:
        upLoadPicture(form_data)
        return "success"
    else:
        return "false"

def ctrlSubmitPic():
    form_data = FieldStorage().encoding.encode()
    if len(form_data) != 0:
        encoded_string = base64.b64encode(form_data)
        upLoadFromLocal(encoded_string)
        return "success"
    else:
        return "false"
