function disp() {
    var c = document.getElementsByTagName("p")
    // if (c.length == 0)
    // {
    //     document.getElementById('hist').innerText = (document.getElementById('hist').innerText + " EMPTY ")
    // }
    for (let l = 0; l < c.length; l++) {
        let d = JSON.parse(c[l].innerText)
        // creating empty text.
        var text=""
        for (let j in d["words"])
        {
            text = text + `<li>${j} : ${d["words"][j]}</li>`
        }
        text = `<ol>${text}</ol>`
        document.getElementsByTagName("p")[l].innerHTML = `<ul><li><b>Text:</b><br> ${d["pragraph"]}</li><br><li><b>Language: </b><br>${d["words_language"]}</li><br><li><b>Vocabulary:</b></li>${text}</ul>`
    }   
}