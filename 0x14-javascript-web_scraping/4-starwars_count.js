#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
