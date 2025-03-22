document.getElementById("btnSubmit").addEventListener("click", function () {

    const textUser = document.getElementById("txtUser").value;

    fetch(`http://127.0.0.1:8005/api/audio/tts?texto=${textUser}`,
        {
            method: "POST",
            headers:{"accept":"application/json"},
        }
    ).then(response => response.blob())
    .then (blob => {

        //create url to blob (audio)

        const audioURL = URL.createObjectURL(blob)

        //create htm audio element
        const audioElement = document.createElement("audio")
        audioElement.src = audioURL
        audioElement.controls = "true"

        //create html control DIV (Container)
        const divContainer = document.createElement("div")
        divContainer.id = "divContainerID"
        divContainer.classList.add("container", "mt-5")

        //adds
        document.body.appendChild(divContainer)
        divContainer.appendChild(audioElement)
        





    })
    .then(data => {
        document.getElementById("txtUser").value = data
    })

})

