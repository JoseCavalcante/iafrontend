document.getElementById("btnSubmit").addEventListener("click", function () {

    const audioInput = document.getElementById("audiofileID");
    const audioFile = audioInput.files[0]

    // transform => bytes
    const formData = new FormData()

    //É preciso adicionar ao formData o arquivo de audio inputado da página
    // veja no backend do projeto que é exigido exatamente este nome de variavel: "file_upload"
    formData.append('file_upload', audioFile) 
    
    fetch('http://127.0.0.1:8005/api/audio/stt_whisper', {
        method: "Post",
        body: formData
    })
    .then(response => response.json()) //Veja no projeto backend que é dito que a resposta chega no formato JSON
    .then(data => {
        document.getElementById("H5transcriptionID").textContent = data
    })

})

