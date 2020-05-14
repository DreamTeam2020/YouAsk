import base64
import cgi
import os
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
    form = cgi.FieldStorage()
    fileitem=form['file']
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        with open(fn, "rb") as image_file:
            encoded_string = base64.b64encode(image_file)
            upLoadFromLocal(encoded_string)
            return fileitem.filename
    else: return "nothing"








'''
# 检测文件是否上传
  if fileitem.filename:
      # 设置文件路径
      print("<p>upload a file</p>")
      fn = os.path.basename(fileitem.filename)
      with open(fn, "rb") as image_file:
          encoded_string = base64.b64encode(fn)
          upLoadFromLocal(encoded_string)
          return encoded_string
'''