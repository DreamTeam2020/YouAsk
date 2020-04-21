def pageStart(title, id):
    # This will generate the start of each html page including the <head></head>

    result = """
        <!DOCTYPE html>
        <html lang="en" id="%s">
            <head>
                <meta charset="utf-8" />
                <title>%s - YouAsk</title>
                <link rel="stylesheet" href="styles/styles.css" />
                <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
            </head>
    """ % (id, title)
    return result

def pageEnd():
    # This will generate the end of each html page, including the <footer>

    result = """
                <footer>
                </footer>
            </body>
        </html>"""

    return result

def generateNav(page):
    # This will generate the nav bar based on input for each page
    # pass an id, if test==id then result+=same page
    home="home.py"
    questions="questions.py"
    profile="profile.py"
    support="support.py"

    if page=="home":
        home=""
    elif page=="questions":
        questions=""
    elif page=="profile":
        profile=""
    elif page=="support":
        support=""

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
