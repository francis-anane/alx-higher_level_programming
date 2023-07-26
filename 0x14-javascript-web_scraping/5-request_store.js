#!/usr/bin/node

/* Get's a web page and stores it in a file */

const fs = require('fs'); // import file system
const request = require('request'); // import request module

if (process.argv.length === 4) {
  const url = process.argv[2]; // The web page to get
  const FILE_PATH = process.argv[3]; // path to save web page
  // Make an http Get request
  request.get(url, (err, response, body) => {
    if (!err) {
    /* Write body in utf-8 encoding mode to file FILE_PATH */
      fs.writeFile(FILE_PATH, body, 'utf-8', err => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
