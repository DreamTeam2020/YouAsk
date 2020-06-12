from controller.html_functions import loginToAccess
from controller.ctrl_cache import *
from controller.ctrl_picture import getProfilePicture
from model.model_functions import getConnections, getUserDetails

def controllerConnections():
    page_name = 'connections'

    result = loginToAccess(False)
    logged = verifyLoggedIn('username', False)

    if logged != 'UNVERIFIED':
        savePageToSession(page_name, False)  # Save the current page to the visitor's session store
        result = generateConnectionsDisplay(logged, 0, False)

    return result

def generateConnectionsDisplay(username, num_connections, sub_dir):
    # Given a number of connections, display that many connections
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix = '../' if sub_dir else ''

    connections = getConnections(username)

    if num_connections == 0:    # If 0 is passed in as the number of connections then display all connections
        num_connections = len(connections)

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
                    """ % (picture, prefix, username, display_name, date, score)

        result += """
                    </section>
                """
    return result

if __name__=='__main__':
    result = generateConnectionsDisplay('Cristian', 0, False)
    print(result)
