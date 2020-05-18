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
    result= verifyLoggedIn('username',False)
    if result=='UNVERIFIED':
        return result
    else:
        form = cgi.FieldStorage()

        if(len(form)!=0):
            fileitem = form['myfile']

            if fileitem.filename:

                fn = os.path.basename(fileitem.filename)
                with open('/tmp/' + fn, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    upLoadFromLocal(result, encoded_string)
                    return encoded_string











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
          
          
def ctrlSubmitPic():
    form = cgi.FieldStorage()
    # 获取文件名
    if(len(form)!=0):
        fileitem = form['myfile']
        # 检测文件是否上传
        if fileitem.filename:
            # 设置文件路径
            fn = os.path.basename(fileitem.filename)
            with open('/tmp/' + fn, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                upLoadFromLocal(encoded_string)
                return encoded_string     
                
                
通过getvalue可以直接得到值     
'''