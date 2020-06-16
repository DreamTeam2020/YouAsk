#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_chat import conctrollerchat


enable()

from controller.html_functions import *

page_name = "chat"

print('Content-Type: text/html')
print()
result = conctrollerchat()

print("""
    %s
    <body>
<script>
function myfunction() {
  setInterval(function(){ alert("Hello"); }, 3000);
}
myfunction();
</script>

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

        %s
    """ % (pageStart("chat", page_name, False), generateHeader(False), generateNav(page_name, False), result,
           generateAsideRight(False), pageEnd()))
