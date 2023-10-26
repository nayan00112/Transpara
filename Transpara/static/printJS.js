var he = `
<style>
.heading {
    font-size: 3.5rem;
    color: black;
    font-weight: bolder;
    display: block;
    margin: 0px;
    padding: 0px;
    color: rgb(64, 64, 255);
}
</style>
<div>
        <h1 class="heading">Transpara</h1>
        <h3 class="lite">Expand your vocabulary</h3>
</div>
`;

function myprint() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML = he + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('DictWordsTable').innerHTML + "<br><hr><br>" + document.getElementById("fr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}

function meaningsprint() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML =  he + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('divmeaning').innerHTML + "<br><br>" + document.getElementById("fr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}

function printWhole() {
    var t = document.getElementsByTagName('body')[0].innerHTML
    document.getElementsByTagName('body')[0].innerHTML =  he + "" + document.getElementById('PragraphText').innerHTML + document.getElementById('DictWordsTable').innerHTML + document.getElementById('divmeaning').innerHTML + "<br><br>" + document.getElementById("fr").innerHTML
    window.print()
    document.getElementsByTagName('body')[0].innerHTML = t
}