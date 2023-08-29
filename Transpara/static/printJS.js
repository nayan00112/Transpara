function myprint() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML = document.getElementById('hed').innerHTML + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('DictWordsTable').innerHTML + "<br><br>" + document.getElementById("footr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}

function meaningsprint() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML = document.getElementById('hed').innerHTML + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('divmeaning').innerHTML + "<br><br>" + document.getElementById("footr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}

function printWhole() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML = document.getElementById('hed').innerHTML + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('DictWordsTable').innerHTML + document.getElementById('divmeaning').innerHTML + "<br><br>" + document.getElementById("footr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}