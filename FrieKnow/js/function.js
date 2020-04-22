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
    $("h2").css('visibility','visible');
}
function Submit() {
    $("h2").css('visibility','hidden');
    var i=0;

    var oneone=$("input").val();
    console.log(oneone);
    var para = document.createElement("p");
    para.innerHTML=oneone;
    document.body.appendChild(para);

   // document.getElementsByTagName("p")[0].innerHTML = oneone;





    // var t = document.createTextNode(oneone);
    // para.appendChild(t);
   // $('p').var("修改内容");
   // document.write("hello");
}