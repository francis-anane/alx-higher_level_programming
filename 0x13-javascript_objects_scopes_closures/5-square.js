#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/* Square class, inherits(extends) Rectangle class */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
