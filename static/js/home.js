$(document).ready(function(){
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
