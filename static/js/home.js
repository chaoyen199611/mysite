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

    

});

const basecard = document.querySelector(".project-block");

$(function(){
    $("#id_category").on("change", function() {
        let selectedValue = $(this).val();
        console.log(selectedValue);
        $.ajax({
            type:"GET",
            url:$("#create-post").attr("action"),
            data : {
                "category": selectedValue
            },
            dataType: 'json',
            success:function(response){
                $('#category-chose').text(response[selectedValue])
                console.log(response["foo"])
            },
            failure: function() {console.log("Error");}
        });
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
                
                let all = document.querySelector(".card-list");
                all.innerHTML="";
                $.each(rep, function(m,item){  
                    console.log(item) 
                    const clone = basecard.cloneNode(true);
                    let img=clone.querySelector(".card-image");
                    img.src="/media/"+item.fields.thumbnail;
                    let category = clone.querySelector("#post-category");
                    category.textContent = item.fields.category;
                    let link = clone.querySelector(".post-link");
                    link.textContent = item.fields.title;
                    if(category.textContent == "Project"){
                        category.style.color = "#154c79";
                        link.href = '/projects/'+item.pk;
                    }
                    else if(category.textContent == "Travel"){
                        category.style.color = "#de7010";
                        link.href = '/travel/'+item.pk;
                    }
                    else if(category.textContent == "Photo"){
                        category.style.color = "#6e14b8";
                    }
                    else{
                        category.style.color = "#b814b2";
                    }
                    
                    let update_time = clone.querySelector(".update-time");
                    update_time.textContent = item.fields.post_time;
                    all.appendChild(clone);
                });
            },
            failure: function() {console.log("Error");}
        });
    });
});

function PreviewImage() {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_thumbnail").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("preview-image").src = oFREvent.target.result;
    };
};
