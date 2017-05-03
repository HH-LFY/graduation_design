


function initData(){
}

function addClick(){
    $('#img-praise').click(function(){
        url = "/praise_img?img_id=" + DATA['img_id'];
        $.get(url,
            function(data,status){
            alert(data);
        });
    });
    $('#img-like').click(function(){
        alert('like');
    });
    $('#img-down').click(function(){
        alert('down');
    });
}


$(document).ready(function(){
    initData();
    addClick();
});