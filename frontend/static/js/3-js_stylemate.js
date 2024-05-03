$(document).ready(function () {
  $('button.submit').click(function () {
    $('#describeform').trigger('submit');
  });
  $('#describeform').submit(function (event) {
    event.preventDefault();
    const descForm = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/get_description',
      method: 'POST',
      data: descForm,
      processData: false,
      contentType: false,
      success: function (response) {
        $('button.submit').text(JSON.stringify(response));
	$('#submit_status').show(10);
      },
      error: function (err, errStr) {
        $('button.submit').text(errStr);
      }
    });
  });
});
