let section = 0;
$(document).ready(function() {
    let form = $('#create-post');
    let addButton = $('#add-field');
    
    addButton.click(function() {
        section++;
        console.log(section);
    });
});

function PreviewImage() {
    let oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_thumbnail").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("preview-image").src = oFREvent.target.result;
    };
};