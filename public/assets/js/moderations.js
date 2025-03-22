document.getElementById("btnSubmit").addEventListener("click", function () {

    const moderation = document.getElementById("txtUser").value;

    fetch(`http://127.0.0.1:8005/api/text/moderation?msg=${moderation}`,
        {
            method: "POST",
            headers:{"accept":"application/json"},
        }
    ).then(response => response.json())
    .then(data => {
        document.getElementById("txtCard").textContent = JSON.stringify(data.results[0].categories)
    })

})

