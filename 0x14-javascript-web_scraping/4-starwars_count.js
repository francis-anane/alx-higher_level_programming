#!/usr/bin/node

/* Display the number of star war movies where the character “Wedge Antilles” is present */

const request = require('request'); // import request module
if (process.argv.length === 3) {
  const url = process.argv[2]; // Star wars api url by alx
  // Make an http Get request
  request.get(url, (err, response, body) => {
    if (!err) {
      const result = JSON.parse(body).results;
      let count = 0;
      for (let i = 0; i < result.length; i++) {
        // console.log(result[i].characters)
        for (let j = 0; j < result[i].characters.length; j++) {
          if (result[i].characters[j].endsWith('/people/18/')) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
