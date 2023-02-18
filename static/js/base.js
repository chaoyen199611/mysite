$(".navbar-nav .nav-item a").on("click", function(){
    $(".nav-item").find(".active").removeClass("active");
    $(this).parent('a').addClass("active");
});