
$.ajax({
    url: $('#get_json').val(), type: 'GET', cache: true,
    success: function (data) {        
        JSON_PATH = data;
        console.log(JSON_PATH)
    }
})



