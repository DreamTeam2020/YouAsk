import base64
import cgi
import os
from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn
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
    result = verifyLoggedIn('username', False)
    message=''
    contents=''
    if result == 'UNVERIFIED':
        return result
    else:
        form = cgi.FieldStorage()


        if (len(form) != 0):

            fileitem = form['myfile']


            if fileitem.filename:

                fn = os.path.basename(fileitem.filename)
             #   fp=open('/tmp/' + fn, 'wb').write(fileitem.file.read())
                encoded_string = base64.b64encode(fileitem.file.read())
                upLoadFromLocal(result, encoded_string)
                return encoded_string

            else:
                message = 'file not success'
        return message

