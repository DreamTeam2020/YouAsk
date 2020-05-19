import base64
import cgi
import os
from cgi import FieldStorage, escape

from controller.ctrl_cache import verifyLoggedIn
from model.model_functions import upLoadPicture, upLoadFromLocal, getPictureCode

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

def getProfilePicture(sub_dir):
    # Get the username, get the profile picture from the
    # database, if none there then display blank image else display profile picture

    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    username = verifyLoggedIn('username', False)

    picture_code = getPictureCode(username)
    profile_picture='%simages/unavailable.png' % prefix

    if picture_code == 'EMPTY':
        result = """
            <figure>
                <img src="%s" title="Blank Profile Picture" alt="A simplistic blank profile picture, depicting a simple grey circle above a grey half ellipse which resembles a person."/>
                <figcaption>
                    <small>
                        (<a href="https://creativecommons.org/share-your-work/public-domain/cc0/">Licensed Under CC0</a>)
                    </small>
                </figcaption>
            </figure>
        """ % profile_picture
    elif picture_code == 'SERVER_ERROR':
        result = '<p class="error">Server Error Occurred</p>'
    else:
        result = """
            <figure>
                <img src="data:image/png;base64, %s" title="User's Profile Picture" alt="This image was uploaded by the user, therefore there is no description available."/>
            </figure>
        """ % picture_code

    return result


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