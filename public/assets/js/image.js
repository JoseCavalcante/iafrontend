document.getElementById("btnSubmit").addEventListener("click", function () {

    const textUser = document.getElementById("txtUser").value;

    fetch(`http://127.0.0.1:8005/api/text/imagegenaration?msg=${textUser}`,
        {
            method: "POST",
            headers:{"accept":"application/json"},
        }
    ).then(response => response.json())
    .then(data => {
        document.getElementById("txtUser").value = data
    })

})

