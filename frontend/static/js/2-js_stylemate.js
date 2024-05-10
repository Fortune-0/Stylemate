$(document).ready(function () {
  $('button').click(function () {
    const themeStr = $(this).text(); // Retrieve the text content of the button
    const str1 = 'http://0.0.0.0:5000/api/v1/outfit/';
    const urlStr = str1.concat(themeStr.trim()); // Trim any leading/trailing whitespace from the themeStr
    $.ajax({
      url: urlStr,
      type: 'GET',
      dataType: 'json',
      success: function (response) {
        $('#displayP').text(JSON.stringify(response));
      },
      error: function (xhr, err, errStr) {
        $('div.display').text(`An error occurred. (${err}) Try restarting app.`);
      }
    });
  });
});
