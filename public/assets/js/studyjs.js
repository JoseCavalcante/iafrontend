
const txt_value = document.getElementById("fname").value;
console.log(txt_value);

document.getElementById("btnSubmit").addEventListener("click", myFunction);

function myFunction() {
    const txt_value = document.getElementById("fname").value;
    console.log(txt_value);

    document.getElementById("fname2").value = document.getElementById("fname").value
}


document.getElementById("btnSubmit2").addEventListener("click", function(event) {

    event.preventDefault();
    
    const textarea = document.createElement("textarea")
    textarea.value="Olá"

    const bt2 = document.getElementById("btnSubmit2")    

    bt2.parentNode.insertBefore(textarea, bt2.nextSibling)
})