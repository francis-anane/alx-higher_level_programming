#!/usr/bin/node

/* Display the status code of an http request */

const request = require('request'); // import request module

if (process.argv.length === 3) {
  // Make an http Get request
  request.get(process.argv[2], (err, response) => {
    if (!err) {
      console.log('code:', response.statusCode);
    }
  });
}
