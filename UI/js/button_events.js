function deleteEvent(quest_id,btn_id) {
    document.getElementById(quest_id).innerHTML = "";
    document.getElementById(btn_id).innerHTML="";
}

function logInbtnBtnHandler(){
    window.location.href ="questions.html";
}