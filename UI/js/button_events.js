function deleteEvent(quest_id, btn_id) {
    document.getElementById(quest_id).innerHTML = "";
    document.getElementById(btn_id).innerHTML = "";
}

function logInbtnBtnHandler() {
    window.location.href = "questions.html";
}
function makeFavourite(ans_id) {
    document.getElementById(ans_id).className += " fa fa-star";
}
function downvoteAnswer(button_id) {
    //This function will increment or decreament the number of downvotes to the db and render total result on UI
    document.getElementById(button_id).innerHTML();
}
function upvoteAnswer(button_id) {
    //This function will set the number of upvotes to db and render the html like button
    document.getElementById(button_id).innerHTML();
}