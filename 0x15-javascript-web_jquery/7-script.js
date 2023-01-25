$(function(){
    const $character = $('Div#character')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(data) {
            $character.html(`${data.name}`)
        },
        error: function() {
            console.log('error')
        }
    })
});