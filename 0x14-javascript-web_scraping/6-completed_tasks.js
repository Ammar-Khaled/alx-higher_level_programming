#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

const data = {};

request(url, (error, response) => {
  if (error == null) {
    const todos = JSON.parse(response.body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (data[todos[i].userId] === undefined) {
          data[todos[i].userId] = 0;
        }
        data[todos[i].userId]++;
      }
    }
  }
  console.log(data);
});
