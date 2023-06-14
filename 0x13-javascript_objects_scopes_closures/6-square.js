#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  /* Prints the rectangle using c or "X" if c is undefined */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
