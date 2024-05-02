function getOut () {
  const themeStr = 'formal'; // Retrieve the text content of the button
  const str1 = 'http://0.0.0.0:5000/api/v1/outfit/';
  const urlStr = str1.concat(themeStr.trim()); // Trim any leading/trailing whitespace from the themeStr
  $.ajax({
    url: urlStr,
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      console.log('new' + JSON.stringify(response));
      $('#displayP').text(JSON.stringify(response));
    },
    error: function (err, errStr) {
      console.log(errStr);
      $('div.display').text(errStr);
    }
  });
}
$('.theme3 button').click(function () {
  getOut();
});
