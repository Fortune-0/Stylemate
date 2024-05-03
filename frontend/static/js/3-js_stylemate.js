$(document).ready(function () {
  $('button.submit').click(function () {
    $('#describeform1').trigger('submit');
    $('#describeform2').trigger('submit');
  });
  $('#describeform1').submit(function (event) {
    event.preventDefault();
    const descForm1 = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/get_description',
      method: 'POST',
      data: descForm1,
      processData: false,
      contentType: false,
      success: function (response) {
        $('#submit_status').text(JSON.stringify(response));
        $('#submit_status').show(10);
      },
      error: function (err, errStr) {
        $('button.sub').text(errStr);
      }
    });
  });
  $('#describeform2').submit(function (event) {
    event.preventDefault();
    const descForm2 = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/get_description',
      method: 'POST',
      data: descForm2,
      processData: false,
      contentType: false,
      success: function (response) {
        $('#submit_status').show(10);
      },
      error: function (err, errStr) {
        $('button.sub').text(errStr);
      }
    });
  });
});
