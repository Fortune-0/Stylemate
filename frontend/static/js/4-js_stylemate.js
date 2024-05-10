$(document).ready(function () {
  $('#userinfo').submit(function (event) {
    event.preventDefault();
    const userForm = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/set_user',
      method: 'POST',
      data: userForm,
      processData: false,
      contentType: false,
      success: function (response) {
        $('.submitstatus').text(response);
        $('.submitstatus').show(10);
        window.location.href = "/";
      },
      error: function (xhr, err, errStr) {
        $('.submitstatus').text(errStr);
        $('.submitstatus').show(10);
      }
    })
  });
});
