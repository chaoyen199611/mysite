const btn = document.getElementById('backtotopbtn');

$(document).ready(function(){
    $(".navbarlist").removeClass("active");
    
});



$(window).scroll(function() {
  console.log($(window).scrollTop());
  if ($(window).scrollTop() > 300) {
    btn.classList.add('show');
  } else {
    btn.classList.remove('show');
  }
});

btn.addEventListener('click', scrollToTop);

function scrollToTop() {
  // Scroll to the top of the page using the "smooth" behavior option
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}
