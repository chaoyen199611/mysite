let section = 0;
$(document).ready(function() {
    let form = $('#create-post');
    let addButton = $('#add-field');
    
    addButton.click(function() {
        section++;
        console.log(section);
        let inputName = 'Section' + section;
        console.log(inputName);
        let divblock = '<div class="form-field">'+inputName+'</div>';
        form.append(divblock)
        let newField = $('<input>')
            .attr('name', inputName)
            .attr('type', 'number');
        form.append(newField);
        let sectiontitle = '<div class="form-field">Section Title</div>';
        form.append(sectiontitle)
        newField = $('<input>')
            .attr('name', "sectiontitle").attr('maxlength',100)
            .attr('type', 'text');
        form.append(newField);
        let sectioncontext = '<div class="form-field">Section Context</div>';
        form.append(sectioncontext)
        newField = $('<input>')
            .attr('name', "sectiontitle")
            .attr('type', 'text');
        form.append(newField);
        let sectionimage = '<div class="form-field">Section Image</div>';
        form.append(sectionimage)
        newField = $('<input>')
            .attr('name', "sectionimage").attr('onchange','PreviewImage()').attr('accept','image/*')
            .attr('type', 'file');
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