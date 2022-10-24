document.addEventListener('DOMContentLoaded', function () {
    document.querySelector(".bt").onclick = diwali;
})

let i = -1;
function diwali(){
    i++;
    const f = "Happy Diwali" ;
    document.querySelector("#h1").innerHTML = f.substring(0,i);
    if (i>=12){
        window.location.replace("G:\\education\\Sir_Mvit\\cpl_programmes\\python\\django\\diwali2.html")
    }
}
function redirec(){
    window.location.replace("G:\\education\\Sir_Mvit\\cpl_programmes\\python\\django\\diwali2.html")
}