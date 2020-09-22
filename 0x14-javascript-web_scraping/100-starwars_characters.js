#!/usr/bin/node
const request = require('request');

const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(URL, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const listPeople = JSON.parse(body).characters;
    listPeople.forEach(element => {
      request(element, (error, response, body) => {
        if (error) {
          console.error(error);
        }
        console.log(JSON.parse(body).name);
      });
    });
  }
});
