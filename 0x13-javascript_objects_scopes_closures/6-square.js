#!/usr/bin/node
const Square = require('./5-square');

class Square_1 extends Square{
  constructor(size){
    super(size, size);
    this.size = size;
  }
  charPrint(c){
    if (c){
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square_1;
