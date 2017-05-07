
function download(src,name){
    var $a = $("<a></a>").attr("href", src).attr("download",name);
    $a[0].click();
}

function initData(){
}

function addClick(){
    $('#img-praise').click(function(){
        url = "/op_img?op=点赞&img_id=" + DATA['img_id'];
        $.get(url,
            function(data,status){
            alert(data);
        });
    });
    $('#img-like').click(function(){
        url = "/op_img?op=收藏&img_id=" + DATA['img_id'];
        $.get(url,
            function(data,status){
            alert(data);
        });
    });
    $('#img-down').click(function(){
        url = DATA['img_url'];
        name = DATA['img_name'];
        download(url,name);
    });
}

$(document).ready(function(){
    initData();
    addClick();
});