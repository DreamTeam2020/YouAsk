from controller.ctrl_cache import verifyLoggedIn

def pageStart(title, id, sub_dir):
    # This will generate the start of each html page including the <head></head>
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix='../' if sub_dir else ''

    result = """
        <!DOCTYPE html>
        <html lang="en" id="%s">
            <head>
                <meta charset="utf-8" />
                <title>%s | YouAsk</title>

                <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
            </head>
    """ % (id, title)
    # <link rel="stylesheet" href="styles/styles.css" />
    return result


def pageEnd():
    # This will generate the end of each html page, including the <footer>

    result = """
                <footer>
                </footer>
            </body>
        </html>"""

    return result


def generateHeader(sub_dir):
    # This will generate the header for each page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    display_name=verifyLoggedIn(sub_dir)
    result="""
            <header>    <!-- A header section displayed at the top of the page--->
                <h1>YOUASK HEADER</h1>
    """
    if display_name=='UNVERIFIED':
        result+="""
                    <section>
                        <p><a href='%slogin.py'>Login</a> | <a href='%sregister.py'>Register</a></p>
                    </section>
        """ % (prefix, prefix)
    else:
        result+="""
                    <section>
                        <p><a href='%sprofile.py'>%s</a> | <a href='%slogout.py'>Logout</a></p>
                    </section>
        """ % (prefix, display_name, prefix)

    result+="""
            </header>
    """
    return result


def generateNav(page, sub_dir):
    # This will generate the nav bar based on input for each page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix='../' if sub_dir else ''

    home = "%sindex.py" % prefix
    questions = "%squestions.py" % prefix
    profile = "%sprofile.py" % prefix
    support = "%ssupport.py" % prefix

    if page == "home":
        home = ""
    elif page == "questions":
        questions = ""
    elif page == "profile":
        profile = ""
    elif page == "support":
        support = ""

    return """
        <nav>
            <ul>
                <li><a href="%s">Home</a></li>
                <li><a href="%s">Questions</a></li>
                <li><a href="%s">Profile</a></li>
                <li><a href="%s">Support</a></li>
            </ul>
        </nav>
        """ % (home, questions, profile, support)


def loginToAccess(sub_dir):
    # If the user is not logged in this will be displayed
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix='../' if sub_dir else ''

    error_msg = """
        <section
            <p class="Error">To access this you must be logged in, you may do so here: </p>
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
        <p class="Error">You are already logged in.</p>
        <p><a href="logout.py">Logout Here</a></p>
    """
    return error_msg


def generateQuestionForm(url, question, description, fields, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!-- Question, Description -->
                <legend>Submit a Question</legend>

                <label for="question">Question: </label>
                <input type="text" name="question" id="question" value="%s" maxlength="300"/>

                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>
    """ % (url, question, description)

    for row in fields:
        # For the id's use the field name in lower case and replace spaces with underscores
        field_code=row['field'].lower().replace(' ', '_')
        field_code+='~%s' % table_name

        result+="""
                    <input type="checkbox" name="fields_of_study" id="%s" value="%s"/>
                    <label for="%s">%s</label>
        """ % (field_code, field_code, field_code, row['field'])

    result+="""
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

                    <label for="answer">Answer: </label>
                    <input type="text" name="answer" id="answer" value="%s"/>

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
                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>
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
                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>
                <label for="email">Your email: </label>
                <input type="text" name="email" id="email" value="%s"/>
                <input type="submit" value="Submit Bug"/>
            </fieldset
        </form>
        %s

    """ % (url, description, email, error)

    return result

def generateEditDetailsForm(url, details, new_display_name, old_password, new_password1, new_password2, error_messages):
    # Generate the form that will allow the user to change some of their details
    result = """
        <section>
            <form action="%s" method="post">
                <fieldset>
                    <p>Username: %s</p>
                    <p>Email: %s</p>
                    <p>Display Name: %s</p>
                    <p>To Edit Your Fields of Study Click <a href="edit_study.py">Here</a></p>
                    
                    <label for="new_display_name">New Display Name: </label>
                    <input type="text" name="new_display_name" id="new_display_name" value="%s" maxlength="35"/>
                    %s
                    
                    <label for="old_password">Current Password: </label>
                    <input type="password" name="old_password" id="old_password" value="%s"/>
                    %s
                    <label for="password1">New Password: </label>
                    <input type="password" name="password1" id="password1" value="%s"/>
                    <label for="password2">Re-Enter New Password: </label>
                    <input type="password" name="password2" id="password2" value="%s"/>
                    %s
                    
                    <input type="submit" value="Update"/>
                </fieldset>
            </form>
            %s
        </section>
    """ % (url, details['username'], details['email'], details['display_name'], new_display_name, error_messages[0],
           old_password, error_messages[1], new_password1, new_password2, error_messages[2], error_messages[3])

    return result

def generateFieldHeadingsForm(url, error_msg):
    # Generate radio form that will contain the 4 main fields of study
    result="""
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
        </section
    """ % (url, error_msg)

    return result

def generateStudyFieldsForm(table_name, url, fields, user_fields, error_msg):
    # Generate the checklist form containing all sub fields of study within the given field

    result="""
        <section>
            <form action ="%s" method="post">
                <fieldset>
    """ % url

    for row in fields:
        # For the id's use the field name in lower case and replace spaces with underscores
        field_code=row['field'].lower().replace(' ', '_')
        field_code+='~%s' % table_name
        checked=False

        for sub_row in user_fields:
            # If a field in the overall list is found in the user's list of fields, then set checked on input
            if row['field'].lower()==sub_row['field'].lower():
                result += """
                            <input type="checkbox" name="fields_of_study" id="%s" value="%s" checked/>
                            <label for="%s">%s</label>
                """ % (field_code, field_code, field_code, row['field'])
                user_fields.remove(sub_row)
                checked=True

        if not checked:
            result+="""
                            <input type="checkbox" name="fields_of_study" id="%s" value="%s"/>
                            <label for="%s">%s</label>
            """ % (field_code, field_code, field_code, row['field'])

    result+="""
                    <input type="submit" value="Select Fields"/>
                </form>
            </fieldset>
            %s
        </section>
    """ % error_msg

    return result

if __name__=="__main__":
    from model.model_functions import *
    # append main_fields to ask_ and get all fields from that table

    table_name = "ask_humanities"
    # Get all fields from table_name
    fields = getFieldsOfStudy(table_name)

    url='edit_study.py'
    error_msg="<p> </p>"
    # Pass fields into a html_functions function and have it loop
    # through the dict adding a label and input each round
    result = generateStudyFieldsForm(table_name, url, fields, error_msg)
    print(result)