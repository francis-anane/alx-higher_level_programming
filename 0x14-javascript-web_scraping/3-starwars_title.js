#!/usr/bin/node

/* Display the title of a star wars movie based on epesode number passed as cli arg */

const request = require('request'); // import request module
const url = 'https://swapi-api.alx-tools.com/api/films/'; // Star wars api url by alx
if (process.argv.length === 3) {
  // Make an http Get request
  request.get(url + process.argv[2], (err, response, body) => {
    if (!err) {
      const film = JSON.parse(body);
      console.log(film.title);
    }
  });
}
