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

  /* Exchange width and height of Rectangle */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /* Multiply width and height of Rectangle by 2 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
