/* fetches a character name from this the star wars movie with the give url with JQuery */
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (content) {
  $('DIV#character').text(content.name);
});
