function alert_error(obj) {
    var html = '';
    $.each(obj, function (key, value) {
        html += '<li>' + key + ': ' + value + '</li>';

    });
//    console.log(html);
    return (html);
}

function alert_jqueryconfirm() {
    $.confirm({
        title: 'Confirm!',
        content: 'Simple confirm!',
        buttons: {
            confirm: function () {
                $.alert('Confirmed!');
            },
            cancel: function () {
                $.alert('Canceled!');
            },
            somethingElse: {
                text: 'Something else',
                btnClass: 'btn-blue',
                keys: ['enter', 'shift'],
                action: function () {
                    $.alert('Something else?');
                }
            }
        }
    });
}