#!/usr/local/bin/python3

from cgitb import enable

enable()

from controller.html_functions import *
from controller.ctrl_saved import *

page_name = "saved"

result = controllerSaved()

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        %s
        %s

        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >.col</aside>

                <main class="col-6 bg-secondary" >
                    <form action="%s.py" method="post">
                        <fieldset>
                            <input type="radio" id="chk_earliest" name="chk_sorting" value="Earliest">
                            <label for="chk_earliest">Earliest</label>

                            <input type="radio" id="chk_latest"  name="chk_sorting" value="Latest" checked>
                            <label for="chk_latest">Latest</label>

                            <input type="submit" value="Sort"/>
                        </fieldset>
                    </form>
                    %s  
                </main>
                %s
            </div>
        </div>

        %s
    """ % (pageStart("Saved", page_name, False), generateHeader(False), generateNav(page_name, False), page_name, result, generateAsideRight(False), pageEnd()))



