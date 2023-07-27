#!/usr/bin/node

/* Display list of characters in a star war movie based on film id passed as cli arg */

const request = require('request'); // import request module
const FILM_URL = 'https://swapi-api.alx-tools.com/api/films/'; // Star wars api url by alx

if (process.argv.length === 3) {
  // Make an http Get request to film
  request.get(FILM_URL + process.argv[2], (err, response, body) => {
    if (!err) {
      const film = JSON.parse(body);
      const characters = film.characters; // Get characters urls
      for (const url in characters) {
        // Make an http Get request to people
        request.get(characters[url], (err, response, body) => {
          if (!err) {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}
