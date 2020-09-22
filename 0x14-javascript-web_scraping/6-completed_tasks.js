#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    const task = JSON.parse(body);
    const infoTasks = {};
    task.forEach(element => {
      if (element.completed === true) {
        if (infoTasks[element.userId] === undefined) {
          infoTasks[element.userId] = 1;
        } else {
          infoTasks[element.userId]++;
        }
      }
    });
    console.log(infoTasks);
  }
});
