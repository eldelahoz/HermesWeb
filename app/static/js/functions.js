function alert_error(obj){
    var html = '';
    $.each(obj, function (key, value){
        html += '<li>' + key + ': ' + value + '</li>';

    });
//    console.log(html);
    return(html);
}