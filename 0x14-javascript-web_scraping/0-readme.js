#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log('Error:', err);
  } else {
    console.log(data.toString());
  }
});
