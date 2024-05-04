$(document).ready(function () {
    $('#describeform1, #describeform2').submit(function (event) {
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
                $('#submit_status').text(errStr);
                $('#submit_status').show(10);
            }
        });
    });
});
