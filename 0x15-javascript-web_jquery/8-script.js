$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      const movies = response.results;
      let movieList = '';
      $.each(movies, function (index, movie) {
        movieList += '<li>' + movie.title + '</li>';
      });
      $('#list_movies').html(movieList);
    },
    error: function () {
      $('#list_movies').html('<li>Failed to fetch movie titles</li>');
    }
  });
});
