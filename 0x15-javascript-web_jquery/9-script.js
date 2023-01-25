$(function(){
    const $hello = $('DIV#hello')
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function(body) {
            let hello = body["hello"];
            $hello.html(hello);
        },
        error: function() {
            console.log('error');
        }
    });
});
