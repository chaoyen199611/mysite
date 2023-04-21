$(document).ready(function(){
    const category = document.querySelectorAll("#post-category").forEach(function (el){
        console.log(el.textContent);
        if(el.textContent == "Project"){
            el.style.color = "#154c79";
        }
        else if(el.textContent == "Travel"){
            el.style.color = "#de7010";
        }
        else if(el.textContent == "Photo"){
            el.style.color = "#6e14b8";
        }
        else{
            el.style.color = "#b814b2";
        }
    });
    $.ajax({          
        type:"GET",
        url:$(".sidebar").attr("data-url"),
        data : {
            "selection": "All"
        },
        dataType: 'json',
        success:function(response){
            var rep = JSON.parse(response);
            $.each(rep, function(m, item){
                console.log(m,item);
            });
        },
        failure: function() {console.log("Error");}
    });
});

$(function() {
    $(".latest-nav").click(function() {
        $(".latest-nav").removeClass("active");
        $(this).addClass("active");
        $.ajax({
            
            type:"GET",
            url:$(".sidebar").attr("data-url"),
            data : {
                "selection": $(this).text()
            },
            dataType: 'json',
            success:function(response){
                
                let rep = JSON.parse(response);
                console.log(rep);
                $.each(rep, function(m, item){
                   
                });
            },
            failure: function() {console.log("Error");}
        });
    });
});

