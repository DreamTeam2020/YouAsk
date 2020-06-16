#!/usr/local/bin/python3

from cgitb import enable

from controller.ctrl_chat import conctrollerchat
from model.model_functions import getMessage

enable()

from controller.html_functions import *

page_name = "chat"

print('Content-Type: text/html')
print()
result = conctrollerchat()
Message=getMessage("CYCYCY4", "Cristian")
Message2=getMessage("Cristian", "CYCYCY4")

print("""
    %s
    <body>
    function myfunction() {
        setInterval(function()
        {            
          $(".aside").html("Message:"+k+%s+%s);
            k=k+1; }, 3000);
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
    """ % (pageStart("chat", page_name, False), Message,Message2,generateHeader(False), generateNav(page_name, False), result,
           generateAsideRight(False), pageEnd()))
