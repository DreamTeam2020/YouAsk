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
        
        <script>
    function myfunction() {
    var k=1;
        setInterval(function()
        {            
          $(".col-3 ").html("%s");
            k=k+1; }, 3000);
    }
    myfunction();
</script>

        %s
    """ % (pageStart("chat", page_name, False), generateHeader(False), generateNav(page_name, False), result,
           generateAsideRight(False),Message,pageEnd()))
