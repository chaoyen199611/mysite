
$(document).ready(function(){
    $(".homenavbar").addClass("active");
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

const options = {
	rootMargin: "0px",
    threshold: 1.0
};

const handleIntersect = (entries, observer) => {
	entries.forEach((entry,index) => {
		const target = entry.target;
        console.log(target);
		if (entry.isIntersecting) {
			target.style.setProperty("--transition", "1.5s");
			target.style.setProperty("--opacity", "1");
			target.style.setProperty("--translate", "translate(0)");
		}
        if (index < entries.length - 1) {
            const nextEntry = entries[index + 1];
            if (nextEntry.intersectionRatio === 1) {
              observer.unobserve(target);
              observer.observe(nextEntry.target);
            }
        }
	});
};
const intersectorSentries = document.querySelectorAll(".event");

const observer = new IntersectionObserver(handleIntersect, options);
intersectorSentries.forEach((sentry) => observer.observe(sentry));

let element;
if($('.aoi-img:visible').length == 0){
    element = document.querySelector(".aoi-img-responsive");
}else{
    element = document.querySelector(".aoi-img");
}

function change() {
    element.classList.toggle("transform-state");
}
  
let imgobserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
        if (entry.intersectionRatio === 1) {
            console.log(entry.target);
            change(); // Call the function when the target object is fully in the viewport
            imgobserver.unobserve(entry.target);
        }
    });
},options);
  
  // Start observing the target object
imgobserver.observe(element);