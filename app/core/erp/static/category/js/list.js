var tblClient;
var getData = () => tblClient = $('#tablaClient').DataTable({
    ajax: {
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
        dataSrc: ''
    },
    columns: [
        {"data": "id"},
        {"data": "nombres"},
        {"data": "apellidos"},
        {"data": "dni"},
        {"data": "fecha_nac"},
        {"data": "sexo.name"},
        {"data": "opt"},
    ],
    columnDefs: [
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash"></i></a>';
                return buttons;
            }
        },
    ]
});

$(function () {
    getData();
    $('#tablaCategory').DataTable({
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ''
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "desc"},
            {"data": "opt"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/category/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/erp/category/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash"></i></a>';
                    return buttons;
                }
            },
        ]
    });
    // $('#tablaClient').DataTable({
    //     ajax: {
    //         url: window.location.pathname,
    //         type: 'POST',
    //         data: {
    //             'action': 'searchdata'
    //         },
    //         dataSrc: ''
    //     },
    //     columns: [
    //         {"data": "id"},
    //         {"data": "nombres"},
    //         {"data": "apellidos"},
    //         {"data": "dni"},
    //         {"data": "fecha_nac"},
    //         {"data": "sexo"},
    //         {"data": "opt"},
    //     ],
    //     columnDefs: [
    //         {
    //             targets: [-1],
    //             class: 'text-center',
    //             orderable: false,
    //             render: function (data, type, row) {
    //                 var buttons = '<a href="/erp/category/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
    //                 buttons += '<a href="/erp/category/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash"></i></a>';
    //                 return buttons;
    //             }
    //         },
    //     ]
    // });
    $('#btnRegistroClient').on('click', function () {
        $('input[name="action"]').val('add');
        $('#myModalClient').modal('show');
        document.getElementById('formClient').reset();
    });
    $('#formClient').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        $.ajax({
            url: window.location.href,
            method: "POST",
            data: parameters,
            dataType: 'json',
            processData: false,
            contentType: false,
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                $('#myModalClient').modal('hide');
                tblClient.ajax.reload();
                return false;
            }
            $('#myModalClient').modal('hide');
            $('#myModalError').modal('show');
            document.getElementById('alert-message').style.display = 'block';
            document.getElementById('detail-error').innerHTML = alert_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {

        });
    });

    $('#tablaClient tbody')
        .on('click', 'a[rel="edit"]', function () {
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="nombres"]').val(data.nombres);
            $('input[name="apellidos"]').val(data.apellidos);
            $('input[name="dni"]').val(data.dni);
            $('input[name="fecha_nac"]').val(data.fecha_nac);
            $('input[name="direccion"]').val(data.direccion);
            $('select[name="sexo"]').val(data.sexo.id);
            $('#myModalClient').modal('show');
        })
        .on('click', 'a[rel="delete"]', function () {
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            $.confirm({
                title: 'Eliminar',
                content: 'Esta seguro que quiere eliminar este registro?',
                icon: 'fa fa-info',
                buttons: {
                    info: {
                        text: 'Si',
                        btnClass: 'btn-primary',
                        action: function () {
                            $.ajax({
                                url: window.location.href,
                                method: "POST",
                                data: parameters,
                                dataType: 'json',
                                processData: false,
                                contentType: false,
                            }).done(function (data) {
                                if (!data.hasOwnProperty('error')) {
                                    tblClient.ajax.reload();
                                    return false;
                                }
                                $('#myModalClient').modal('hide');
                                $('#myModalError').modal('show');
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
        });

});
