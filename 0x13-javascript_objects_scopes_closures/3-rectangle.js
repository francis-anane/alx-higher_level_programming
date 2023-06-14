#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  /* prints the Rectangle with the character "X" */
  print () {
    const symbol = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(symbol.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
