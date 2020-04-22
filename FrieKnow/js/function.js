//document.write("<script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>");//import jquery

function HomeFunction(){
    $("article").load("Home.html");
}
function QuestionFunction(){
    $("article").load("Question.html");
}
function ProfileFunction(){
    $("article").load("Profile.html");
}
function SupportFunction(){
    $("article").load("Support.html");
}
function Ask() {
    $("h2").css('display','block');
}
function Submit() {
    $("h2").css('display','none');
    var oneone=$("input").val();
   document.getElementById("one").innerHTML = oneone;

   // document.write("hello");
}