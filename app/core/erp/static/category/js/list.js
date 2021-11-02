$(function (){
    $('#tablaCategory').DataTable( {
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
            render: function (data, type, row){
                var buttons = '<a href="/erp/category/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                buttons += '<a href="/erp/category/delete/' + row.id +  '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                return buttons;
            }
        },
        ]
    });
});
