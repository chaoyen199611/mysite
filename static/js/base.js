$(document).ready(function(){
    $(".navbarlist").removeClass("active");
    
});
let btn = $('#backtotopbtn');


// Get the navbar
let navbar = document.getElementById("article-nav");

// Get the offset position of the navbar
//let sticky = navbar.offsetTop;

// window.onscroll = function() {myFunction()};
// // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
  
//   if(window.scrollY>300){
//     btn.addClass('show');
//   }
//   else{
//     btn.removeClass('show');
//   }
//   if (window.scrollY+60 >= sticky) {
//     navbar.classList.add("sticky");
//   } else {
//     navbar.classList.remove("sticky");
//   }
// }


$(window).scroll(function() {
  console.log($(window).scrollTop());
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
  // if ($(window).scrollTop()+60 >= sticky) {
  //   navbar.classList.add("sticky");
  // } else {
  //   navbar.classList.remove("sticky");
  // }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '0');
});






