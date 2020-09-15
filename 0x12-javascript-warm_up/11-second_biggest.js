#!/usr/bin/node

const arg = process.argv;
const listInt = [];
arg.forEach((val, index) => {
  if (index >= 2) {
    listInt.push(parseInt(val, 10));
  }
});

listInt.sort();
console.log(listInt[listInt.length - 2]);
