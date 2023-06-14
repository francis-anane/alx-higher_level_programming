#!/usr/bin/node
/* Rectangle class, creates an empty object if the properties w or h is <= 0 */
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
