$(function(){
    const $list_movies = $('ul#list_movies')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {
            const movies_list = data.results;
            $.each(movies_list, function(i, movie) {
                $list_movies.append('<li>' + movie.title +'</li>')
            })
        },
        error: function() {
            console.log('error')
        }
    })
});