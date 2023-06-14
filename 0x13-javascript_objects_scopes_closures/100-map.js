#!/usr/bin/node

/* Creates a new array from the elements of an array with each new element been
the element multiplied by it index */

const list = require('./100-data').list;
console.log(list);
console.log(list.map((element, index) => element * index));
