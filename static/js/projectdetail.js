let navbar = document.getElementById("article-nav");

$(document).ready(function(){
    $(".projectnavbar").addClass("active");
});



let sticky = navbar.offsetTop;

window.onscroll = function() {myFunction()};
// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  
  if (window.scrollY+60 >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}