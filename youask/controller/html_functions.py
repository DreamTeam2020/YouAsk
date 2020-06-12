
from controller.ctrl_cache import verifyLoggedIn  # This is used, ignore pycharm
from controller.ctrl_search import searchKeyword
from model.model_functions import getQuestionFields

from controller.ctrl_cache import verifyLoggedIn, getLastViewedQuestionFromSession
from model.model_functions import getQuestionFields, getSpecificQuestion, getConnections, getUserDetails, getPictureCode

import json
import requests


def pageStart(title, id, sub_dir):
    # This will generate the start of each html page including the <head></head>
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''



    result = """
            <!DOCTYPE html>
            <html lang="en" id="%s">
                <head>
                    <meta charset="utf-8" />
                    <title>%s | YouAsk</title>
                    <link rel="stylesheet" href="%sbootstrap-4.5.0-dist/css/bootstrap.css">  
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                    <script src="%sbootstrap-4.5.0-dist/js/bootstrap.js"></script>
                    <script src="%sscripts/test.js"></script>
                    <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
                </head>
        """ % (id, title, prefix, prefix, prefix)

    return result


def pageEnd():
    # This will generate the end of each html page, including the <footer>

    result = """
                <footer>
                something about Copyright
                </footer>
            </body>
        </html>"""

    return result


def generateHeader(sub_dir):
    # This will generate the header for each page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    display_name = verifyLoggedIn('display_name', sub_dir)  # Returns display_name if logged in else 'UNVERIFIED'
    result = """
            <header>    <!-- A header section displayed at the top of the page--->
        
    """
    if display_name == 'UNVERIFIED':
        result += """
                    <section>
                        <p><a href='%slogin.py'>Login</a> | <a href='%sregister.py'>Register</a></p>
                    </section>
        """ % (prefix, prefix)
    else:
        profile_page = profilePageLink(sub_dir)
        result += """
                    <section>
                        <p><a href='%s'>%s</a> | <a href='%slogout.py'>Logout</a></p>
                    </section>
        """ % (profile_page, display_name, prefix)

    result += """
            </header>
    """
    return result


def generateNav(page, sub_dir):
    # This will generate the nav bar based on input for each page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    home = "%sindex.py" % prefix
    questions = "%squestions.py" % prefix
    profile = profilePageLink(sub_dir)
    support = "%ssupport.py" % prefix
    result, txt_search = searchKeyword()

    if page == "home":
        home = ""
    elif page == "questions":
        questions = ""
    elif page == "user_profile":
        profile = ""
    elif page == "support":
        support = ""

    return """
        <nav class="container-fluid">
        
            <ul class="navbar navbar-expand-sm  bg-secondary ">
                <a class="navbar-brand " href="%s">YouAsk</a>
                <li class="navbar-nav ">
                    <a class="nav-link" href="%s">Home</a>
                </li>
                <li class="navbar-nav ">
                    <a class="nav-link active" href="%s">Questions</a>
                </li>
                <li class="navbar-nav ">
                    <a class="nav-link active" href="%s">Profile</a>
                </li>
                <li class="navbar-nav">
                    <a class="nav-link" href="%s">Support</a>
                </li>
                 <li class="navbar-nav">
                <form action="%s" method="post">
                        <fieldset>
                            <label for="txt_search">Search: </label>
                            <input type="text" name="txt_search" id="txt_search" value="%s"/>
                            
                            <input type="submit" value="Click to search"/>
                        </fieldset>
                </form>
                </li>
            </ul>
        </nav>
        
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>
              
                <main class="col-6 bg-secondary" >   %s  </main>
               
                <aside class="col bg-primary" >.col</aside>
              
            </div>
        </div>
        """ % (home, home, questions, profile, support,"html_functions.py", txt_search, result)

def generateAsideRight(sub_dir):
    # This will generate the right aside on every page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    result = """
        <aside class="col bg-primary" >
    """

    logged = verifyLoggedIn('username', sub_dir)  # Returns username if logged in else 'UNVERIFIED'
    if logged != 'UNVERIFIED':  # If logged in

        # Last Viewed Question - Display the last viewed question without share links
        question_id = getLastViewedQuestionFromSession(sub_dir)
        if question_id:
            # Get the question from the database and display it accordingly
            last_question = getSpecificQuestion(question_id)
            last_viewed_result = generateQuestionDisplayNoShare(last_question, sub_dir)

        else:
            last_viewed_result = """
                <section>
                    <p>No Recently Viewed Question</p>
                </section>
            """
        result += last_viewed_result

        # Connections List Page
        result += generateConnectionsDisplay(logged, 2, sub_dir)


        # Submitted Question Page
    else:
        result += loginToAccess(sub_dir)

    result += """
        </aside>
    """

    return result


def loginToAccess(sub_dir):
    # If the user is not logged in this will be displayed
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    error_msg = """
        <section>
            <p class="error">To access this you must be logged in, you may do so here: </p>
            <ul>
                <li><a href="%sregister.py">Register</a></li>
                <li><a href="%slogin.py">Log In</a></li>
            </ul>
        </section>
    """ % (prefix, prefix)
    return error_msg


def alreadyLoggedIn():
    # If the user is already logged in and tries to log in
    error_msg = """
        <p class="error">You are already logged in.</p>
        <p><a href="logout.py">Logout Here</a></p>
    """
    return error_msg


def generateQuestionForm(url, question, description, fields, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!-- Question, Description -->
                <legend>Submit a Question</legend>

                <label for="txt_question">Question: </label>
                <input type="text" name="txt_question" id="txt_question" value="%s" maxlength="300"/>

                <label for="txt_description">Description: </label>
                <input type="text" name="txt_description" id="txt_description" value="%s"/>
    """ % (url, question, description)

    for row in fields:
        # For the id's use the field name in lower case and replace spaces with underscores
        field_code = row['field'].lower().replace(' ', '_')

        result += """
                <input type="checkbox" name="fields_of_study" id="%s" value="%s"/>
                <label for="%s">%s</label>
        """ % (field_code, field_code, field_code, row['field'])

    result += """
                <input type="submit" value="Submit Question"/>
            </fieldset
        </form>
        %s
    """ % error

    return result


def generateAnswerForm(url, answer, error):
    # Generate the answer form to be used
    result = """
        <section>
            <form action="%s" method="post">
                <fieldset> <!-- Answer -->
                    <legend>Submit an Answer</legend>

                    <label for="txt_answer">Answer: </label>
                    <input type="text" name="txt_answer" id="txt_answer" value="%s"/>

                    <input type="submit" value="Submit Answer"/>
                </fieldset
            </form>
            %s
        </section>
    """ % (url, answer, error)

    return result


def generateBugreportForm(url, description, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!--  Description -->
                <label for="txt_description">Description: </label>
                <input type="text" name="txt_description" id="txt_description" value="%s"/>
                <input type="submit" value="Submit Bug"/>
            </fieldset
        </form>
        %s
     
    """ % (url, description, error)

    return result


def generateBugreportFormWithEmail(url, description, email, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!--  Description, Email -->
                <label for="txt_description">Description: </label>
                <input type="text" name="txt_description" id="txt_description" value="%s"/>
                
                <label for="txt_email">Your email: </label>
                <input type="text" name="txt_email" id="txt_email" value="%s"/>
                
                <input type="submit" value="Submit Bug"/>
            </fieldset
        </form>
        %s

    """ % (url, description, email, error)

    return result


def generateEditDetailsForm(url, details, user_fields, new_display_name, old_password, new_password1, new_password2,
                            error_messages):
    # Generate the form that will allow the user to change some of their details
    result = """
        <section>
            <form action="%s" method="post">
                <fieldset>
                    <p>Username: %s</p>
                    <p>Email: %s</p>
                    <p>Display Name: %s</p>
                    %s
                    <p>To Edit Your Fields of Study Click <a href="edit_study.py">Here</a></p>
                    <p>To Edit Your Profile Picture Click <a href="profile_picture.py">Here</a></p>
                    
                    <label for="txt_new_display_name">New Display Name: </label>
                    <input type="text" name="txt_new_display_name" id="txt_new_display_name" value="%s" maxlength="35"/>
                    %s
                    
                    <label for="txt_old_password">Current Password: </label>
                    <input type="password" name="txt_old_password" id="txt_old_password" value="%s"/>
                    %s
                    <label for="txt_password1">New Password: </label>
                    <input type="password" name="txt_password1" id="txt_password1" value="%s"/>
                    <label for="txt_password2">Re-Enter New Password: </label>
                    <input type="password" name="txt_password2" id="txt_password2" value="%s"/>
                    %s
                    
                    <input type="submit" value="Update"/>
                </fieldset>
            </form>
            %s
        </section>
    """ % (url, details['username'], details['email'], details['display_name'], user_fields, new_display_name,
           error_messages[0],
           old_password, error_messages[1], new_password1, new_password2, error_messages[2], error_messages[3])

    return result


def generateFieldHeadingsForm(url, error_msg):
    # Generate radio form that will contain the 4 main fields of study
    result = """
        <section>
            <form action="%s" method="post">
                <fieldset>
                    <p>Fields were set up following this <a href="https://en.wikipedia.org/wiki/List_of_academic_fields">format</a></p>
                    <input type="radio" name="fields_of_study" id="humanities" value="humanities"/>
                    <label for="humanities">Humanities and Social Science</label>
                    
                    <input type="radio" name="fields_of_study" id="natural_sciences" value="natural_sciences"/>
                    <label for="natural_sciences">Natural Sciences</label>
                    
                    <input type="radio" name="fields_of_study" id="formal_sciences" value="formal_sciences"/>
                    <label for="formal_sciences">Formal Sciences</label>
                    
                    <input type="radio" name="fields_of_study" id="professions" value="professions"/>
                    <label for="professions">Professions and Applied Sciences</label>
                    
                    <input type="submit" value="Select"/>
                </fieldset>
            </form>
            %s
        </section>
    """ % (url, error_msg)

    return result


def generateStudyFieldsForm(url, fields, user_fields, error_msg):
    # Generate the checklist form containing all sub fields of study within the given field

    result = """
        <section>
            <form action ="%s" method="post">
                <fieldset>
    """ % url

    for row in fields:
        # For the id's use the field name in lower case and replace spaces with underscores
        field_code = row['field'].lower().replace(' ', '_')
        checked = False
        if user_fields != 'EMPTY':
            for sub_row in user_fields:
                # If a field in the overall list is found in the user's list of fields, then set checked on input
                if row['field'].lower() == sub_row['field'].lower():
                    result += """
                                <input type="checkbox" name="fields_of_study" id="%s" value="%s" checked/>
                                <label for="%s">%s</label>
                    """ % (field_code, field_code, field_code, row['field'])
                    user_fields.remove(sub_row)
                    checked = True

        if not checked:
            result += """
                            <input type="checkbox" name="fields_of_study" id="%s" value="%s"/>
                            <label for="%s">%s</label>
            """ % (field_code, field_code, field_code, row['field'])

    result += """
                    <input type="submit" value="Select Fields"/>
                </form>
            </fieldset>
            %s
        </section>
    """ % error_msg

    return result


def shareLinks(sub_dir, question_id):
    # Returns some html that contains images which link to social media for sharing
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    facebook_src = "%simages/facebook.png" % prefix
    twitter_src = "%simages/twitter.png" % prefix

    share_to_fb = """
   
            <a href="https://www.facebook.com/sharer.php?u=https://cs1.ucc.ie/~cgg1/cgi-bin/youask/question_pages/question_%s.py" target="_blank" ;">
                <img src="%s" title="Share to Facebook" alt="An image of the Facebook social media logo, which is a white lowercase letter f on a blue background." style="width:40px;height:40px;"/>
            </a>
    
    """ % (question_id, facebook_src)

    share_to_tw = """
           
                <a href="https://twitter.com/share" target="_blank" data-url=https://cs1.ucc.ie/~cgg1/cgi-bin/youask/question_pages/question_%s.py data-text="" data-via=""data-lang="ja">
                    <img src="%s" title="Share to Twitter" alt="An image of the Twitter social media logo, which is a side view of a light blue, simplistic bird." style="width:40px;height:40px;"/>
                </a>
        
        """ % (question_id, twitter_src)

    result = share_to_fb + share_to_tw

    return result


def generateQuestionsDisplay(questions, sub_dir):
    # Given a list of questions, display them accordingly
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''
    result = """
            <section>
        """

    for question in questions:
        result += """
                    <section class="question">
                        <a href="question_pages/question_%s.py">
                            <p>%s</p>
                        </a>
            """ % (question['id'], question['question'])

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
                            <p><small>Submitted By: <a href='%sprofile_pages/profile_%s.py'>%s</a> | Score: %d | View Count: %d</small></p>
                        %s
                    </section>
            """ % (fields_of_study, prefix, question['submitter'].lower(), question['submitter'], question['score'], question['view_count'], share_links)

    result += """
            </section>
        """

    return result

def generateQuestionDisplayNoShare(question, sub_dir):
    # Given a question (dictionary), display it accordingly
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    result = """
                <section class="question">
                    <a href="question_pages/question_%s.py">
                        <p>%s</p>
                    </a>
        """ % (question['id'], question['question'])

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

    result += """
                        %s
                        <p><small>Submitted By: <a href='%sprofile_pages/profile_%s.py'>%s</a> | Score: %d | View Count: %d</small></p>
                </section>
        """ % (fields_of_study, prefix, question['submitter'].lower(), question['submitter'], question['score'], question['view_count'])

    return result

def profilePageLink(sub_dir):
    # This will be used to set the profile page links on the website to link to the user's profile page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    username = verifyLoggedIn('username', sub_dir)
    if username == 'UNVERIFIED':
        link = "%slogin.py" % prefix
    else:
        link = "%sprofile_pages/profile_%s.py" % (prefix, username.lower())

    return link

def generateNews(num):
    # Generates html code containing various news articles depending on given number
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=1e2203fa10234d0a999cf82f685ac8d2')
    response = requests.get(url)
    convert_data = response.text
    json_data = json.loads(convert_data)

    result = """
        <section>
    """

    for field in range(num):
        title = json_data["articles"][field]["title"].encode()
        description = json_data["articles"][field]["description"].encode()
        # title = title[2:-1]
        # description = description[2:-1]

        result += """
            <article>
                <h1>%s</h1>
                <p>%s</p>
            </article>
        """ % (title, description)

    result += """
        </section>
    """

    return result

def getProfilePicture(username, sub_dir):
    # Get the username, get the profile picture from the
    # database, if none there then display blank image else display profile picture

    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

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

def generateConnectionsDisplay(username, num_connections, sub_dir):
    # Given a number of connections, display that many connections
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    connections = getConnections(username)

    if num_connections == 0:    # If 0 is passed in as the number of connections then display all connections
        num_connections = len(connections)
        connect_link = ""
    else:
        connect_link = "<p>View Your Connections <a href='%sconnections.py'>Here</a></p>" % prefix

    if not connections:
        result = """
                    <section>
                        <p class="error">No Connections Available</p>
                    </section>
                """
    else:
        result = """
                    <section>
                """

        for i in range(num_connections):
            username = connections[i]['friend']
            date = connections[i]['connect_date']
            picture = getProfilePicture(username, False)
            details = getUserDetails(username)
            display_name = details['display_name']
            score = details['score']

            result += """
                        <section>
                            %s
                            <p><a href='%sprofile_pages/profile_%s.py'>%s</a></p>
                            <p><small>Connection Since: %s | User Score: %d</small></p>
                        </section>
                    """ % (picture, prefix, username.lower(), display_name, date, score)

        result += """
                    %s
                    </section>
                """ % connect_link
    return result

if __name__ == "__main__":
    #news = generateNews(7)
    #print(news)
    #question_id = 70
    #last_question = getSpecificQuestion(question_id)
    #question_display = generateQuestionDisplayNoShare(last_question, False)
    #print(question_display)

    result = generateConnectionsDisplay('Cristian', 2, False)
    print(result)