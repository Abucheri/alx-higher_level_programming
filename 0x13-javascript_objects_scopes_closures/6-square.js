#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    const character = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
