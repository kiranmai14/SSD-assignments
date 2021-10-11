const hamburger = document.querySelector(
  ".header .nav-bar .nav-list .hamburger"
);
const mobileMenu = document.querySelector(".header .nav-bar .nav-list .list");
const header = document.querySelector(".header");

function clickhamburgar() {
  mobileMenu.classList.toggle("active");
}
hamburger.addEventListener("click", clickhamburgar);

function onclickHome() {
  document.getElementById("home").style.display = "block";
  document.getElementById("about").style.display = "none";
  document.getElementById("edu").style.display = "none";
  document.getElementById("contact").style.display = "none";
  
}
function onclickAbout() {
  document.getElementById("home").style.display = "none";
  document.getElementById("about").style.display = "block";
  document.getElementById("edu").style.display = "none";
  document.getElementById("contact").style.display = "none";
  header.style.backgroundColor = "rgb(1, 6, 26)";
}
function onclickEdu() {
  document.getElementById("home").style.display = "none";
  document.getElementById("about").style.display = "none";
  document.getElementById("edu").style.display = "block";
  document.getElementById("contact").style.display = "none";
  header.style.backgroundColor = "rgb(1, 6, 26)";
}
function onclickContact() {
  document.getElementById("home").style.display = "none";
  document.getElementById("about").style.display = "none";
  document.getElementById("edu").style.display = "none";
  document.getElementById("contact").style.display = "block";
  header.style.backgroundColor = "rgb(1, 6, 26)";
}

setInterval(function () {
  var date = new Date();
  dateConvert(date);
}, 1);

function dateConvert(date) {
  var n = date.toDateString();
  var time = date.toLocaleTimeString();
  document.getElementById("date").innerHTML = n + " " + time;
}
