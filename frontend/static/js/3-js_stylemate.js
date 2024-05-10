$(document).ready(function () {
    $.ajax({
        url: 'http://0.0.0.0:5000/api/v1/get_display_items',
        method: 'GET',
        dataType: 'json',
        success: function (response) {
            for (let item of response['tops']) {
                const key = Object.keys(item)[0]
                const key_upper = key.charAt(0).toUpperCase() + key.slice(1);
                const vall = item[key];
                const item1 = `<label>${key_upper}</label>`;
                const item2 = $('<input/>', { type: 'number', value: vall, name: key, min: 0 });
                item2.append('<br>');
                const item3 = $('<p></p>').append(item1, item2);
                item3.addClass('forms');
                $('div.form1').append(item3);
            }
            for (let item of response['bottoms']) {
                const key = Object.keys(item)[0]
                const key_upper = key.charAt(0).toUpperCase() + key.slice(1);
                const vall = item[key];
                const item1 = `<label>${key_upper}</label>`;
                const item2 = $('<input/>', { type: 'number', value: vall, name: key, min: 0 });
                item2.append('<br>');
                const item3 = $('<p></p>').append(item1, item2);
                item3.addClass('forms');
                $('div.form2').append(item3);
            }
        },
        error: function (xhr, err, errStr) {
            console.log(errStr);
        }
    });
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
            error: function (xhr, err, errStr) {
                $('#submit_status').text(errStr);
                $('#submit_status').show(10);
            }
        });
    });
});
