#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    try {
      fs.writeFileSync(process.argv[3], body, 'utf-8');
    } catch (error) {
      console.error(error);
    }
  }
});
