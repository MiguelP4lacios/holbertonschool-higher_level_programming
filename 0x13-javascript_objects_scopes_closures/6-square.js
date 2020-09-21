#!/usr/bin/node
const SquareOld = require('./5-square');

class Square extends SquareOld {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c) {
        console.log('C'.repeat(this.size));
      } else {
        console.log('X'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
