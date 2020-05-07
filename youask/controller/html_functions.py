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


def generateQuestionForm(url, question, description, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!-- Question, Description -->
                <legend>Submit a Question</legend>

                <label for="question">Question: </label>
                <input type="text" name="question" id="question" value="%s" maxlength="300"/>

                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>

                <input type="submit" value="Submit Question"/>
            </fieldset
        </form>
        %s
    """ % (url, question, description, error)

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
            <p>To Edit Your Fields of Study Click <a href="edit_study.py">Here</a></p>
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
                    <label for="humanities">Humanities and Social Science</label>
                    <input type="radio" name="main_fields" id="humanities" value="humanities"/>
                    
                    <label for="natural_sciences">Natural Sciences</label>
                    <input type="radio" name="main_fields" id="natural_sciences" value="natural_sciences"/>
                    
                    <label for="formal_sciences">Formal Sciences</label>
                    <input type="radio" name="main_fields" id="formal_sciences" value="formal_sciences"/>
                    
                    <label for="professions">Professions and Applied Sciences</label>
                    <input type="radio" name="main_fields" id="professions" value="professions"/>
                </fieldset>
            </form>
            %s
        </section
    """ % (url, error_msg)

    return result


