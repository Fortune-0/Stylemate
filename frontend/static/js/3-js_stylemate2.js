$(document).ready(function () {
  $('button.sub1').click(function () {
    $('#describeform1').trigger('submit');
  });
  $('button.sub2').click(function () {
    $('#describeform2').trigger('submit');
  });
  $('#describeform1', '#describeform2').submit(function (event) {
    event.preventDefault();
    const descForm = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/get_description',
      method: 'POST',
      data: descForm,
      processData: false,
      contentType: false,
      success: function (response) {
        $('#submit_status').text(JSON.stringify(response));
        $('#submit_status').show(10);
      },
      error: function (err, errStr) {
        $('button.sub1').text(errStr);
      }
    });
  });
});
