#!/usr/bin/node

const arg = process.argv;

if (!arg[2] || arg[2] === '1') {
  console.log(0);
} else {
  const listInt = [];
  arg.forEach((val, index) => {
    if (index >= 2) {
      listInt.push(parseInt(val, 10));
    }
  });

  listInt.sort();
  console.log(listInt[listInt.length - 2]);
}
