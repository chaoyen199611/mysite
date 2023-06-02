let section = 0;
$(document).ready(function() {
    let form = $('#create-post');
    let addButton = $('#add-field');
    let textarea = $('#id_maincontent');

    $(".projectnavbar").addClass("active");

    textarea.on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    const category = document.querySelectorAll(".project-field").forEach(function (el){
        console.log(el.textContent);
        if(el.textContent == "Machine Learning"){
            el.style.background = "aqua";
        }
        else if(el.textContent == "BlockChain"){
            el.style.color = "#de7010";
        }
        else if(el.textContent == "3D Art"){
            el.style.color = "#6e14b8";
        }
        else{
            el.style.color = "#b814b2";
        }
    });
});

function PreviewImage() {
    let oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_thumbnail").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("preview-image").src = oFREvent.target.result;
    };
};

let colorMatch = {
    'Machine Learning':'blue',
    '20-59'    : 'orange',
    '60-100'   : 'green'
 };