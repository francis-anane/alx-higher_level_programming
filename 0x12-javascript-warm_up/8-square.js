#!/usr/bin/node
/* prints a square, the first argument to the script is the size, from a value
that is convertabel to a Number type
*/

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  let counter = 0;
  while (counter < size) {
    console.log('X'.repeat(size));
    counter++;
  }
}
