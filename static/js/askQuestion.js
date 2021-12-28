/* This file will send a post request to `/askQuestion` endpoint of the website to ask a question in website */
let questionTitleValue = document.getElementById('questionTitle').value; // Getting Value of Question Title
let selectCategoryofQuestionElement = document.getElementById('selectCategoryofQuestion'); // Getting Element that selects category
let askAQuestionTextAreaCode = tinymce.get('askAQuestionTextArea').getContent(); // Getting Code of tinymce Textarea
// let selectedCategoryValue = selectCategoryofQuestionElement.options[selectCategoryofQuestionElement]
let askQuestionSubmitButton = document.getElementById('askQuestionSubmitButton');

// Adding Click Event Listener on submit button
askQuestionSubmitButton.addEventListener('click',(event)=>{
    event.preventDefault();
})

// function sendPostRequestAskQuestionFunction(){

// }