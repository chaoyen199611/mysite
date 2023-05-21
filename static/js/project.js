$(document).ready(function() {
    let form = $('#create-post');
    let addButton = $('#add-field');
    
    addButton.click(function() {
        let inputName = 'field' + (form.children().length);
        console.log(inputName);
        let divblock = '<div class="form-field">'+inputName+'</div>';
        form.append(divblock)
        let newField = $('<input>')
            .attr('name', inputName)
            .attr('type', 'text');
        form.append(newField);
    });
});

function PreviewImage() {
    let oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_thumbnail").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("preview-image").src = oFREvent.target.result;
    };
};