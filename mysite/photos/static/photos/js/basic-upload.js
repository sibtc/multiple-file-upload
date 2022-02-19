$(document).ready( function () {
  //https://django-rest-framework-datatables.readthedocs.io/en/latest/tutorial.html#a-more-complex-and-detailed-example
  $('#gallery').DataTable({
  "serverSide": true,
  "ajax": "/photos/api/photos/?format=datatables",
  "columns": [
      {"data": "file", "render": function(data) { return `<img src="${data}" style="height:100px;"/>`;}},
      {"data": "file", "render": function(data) { return `<a href="${data}" style="height:100px;">${data.split('/').pop()}</a>`;}},
      {"data": "uploaded_at"},
  ]
  });
});

$(function () {
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
      $('#gallery').DataTable().ajax.reload();
    }
  });
});