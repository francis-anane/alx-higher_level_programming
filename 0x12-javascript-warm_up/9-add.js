#!/usr/bin/node

/* Add two numbers passed as arguments to the script */

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(Number(process.argv[2]), Number(process.argv[3]));
