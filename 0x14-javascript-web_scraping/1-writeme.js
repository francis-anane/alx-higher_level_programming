#!/usr/bin/node

/* Write's string to file argv[2] is the path to write to and argv[3] is the content */

const fs = require('fs'); // import file system

if (process.argv.length === 4) {
  /* The writeFile in utf-8 encoding mode */
  fs.writeFile(process.argv[2], process.argv[3], 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
}
