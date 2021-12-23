// This javascript file will make sure that no devices other than PCs and laptops can open modal

let noModalButtonArray = document.getElementsByClassName('noModalButtonElement'); // Getting All Buttons that would open the modal

// Checking Wether the width of window is less than 768px to make sure that devices with less width size can't open the modal
if (screen.width <= 768){
    Array.from(noModalButtonArray).forEach((element)=>{
        console.log(element);
        element.removeAttribute('data-bs-target'); // Removing 'data-bs-target' attribute so that modal can't be opened when clicked on the button
        console.log(element);
        element.removeAttribute('data-bs-toggle'); // Removing 'data-bs-toggle' attribute so that modal can't be opened when clicked on the button
        console.log(element);
    })
}

Array.from(noModalButtonArray).forEach((element)=>{
    element.addEventListener('click',()=>{
        if (screen.width <= 768){
            alert('You can ask your question only in a laptop and a computer'); // Poping Up an Alert to remind that user can't open up the modal
        }
    })
})