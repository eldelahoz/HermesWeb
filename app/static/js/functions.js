function alert_error(obj) {
    var html = '';
    $.each(obj, function (key, value) {
        html += '<li>' + key + ': ' + value + '</li>';

    });
//    console.log(html);
    return (html);
}

function alert_jqueryconfirm(url, title, content, parameters, callback) {
    $.confirm({
        title: title,
        content: content,
        icon: 'fa fa-info',
        buttons: {
            info: {
                text: 'Si',
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url,
                        method: "POST",
                        data: parameters,
                        dataType: 'json'
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        document.getElementById('alert-message').style.display = 'block';
                        document.getElementById('detail-error').innerHTML = alert_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: 'No',
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    });
}