#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_chat import conctrollerchat
from model.model_functions import getMessage

enable()

from controller.html_functions import *

import time

page_name = "chat"

print('Content-Type: text/html')
print()
result = conctrollerchat()

i = 1

print("""
    %s
    <body>
        %s
        %s
        <div class="container-fluid">
            <div class="row">
                <aside class="col-3 bg-primary" >
                </aside>
                <main class="col-6 bg-secondary" >   %s  </main>
                %s
            </div>
        </div>
    """ % (pageStart("chat", page_name, False), generateHeader(False), generateNav(page_name, False), result,
           generateAsideRight(False)))


def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleep_time(0, 0, 1)
while True:
    time.sleep(second)
    Message = getMessage("CYCYCY4", "Cristian")
    Message2 = getMessage("Cristian", "CYCYCY4")

    print("""

                <script>

                 $(".col-3 ").html("%s");
                </script>

                %s





        """ % (Message, pageEnd()))