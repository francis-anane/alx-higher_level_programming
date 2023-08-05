/* Fetches and lists the title for all star war movies by using the URL with JQquery */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (content) {
  $('UL#list_movies').append(...content.results.map(movie => `<li>${movie.title}</li>`));
});
