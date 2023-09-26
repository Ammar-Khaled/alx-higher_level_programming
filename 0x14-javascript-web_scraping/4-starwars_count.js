#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(response.body).films.length);
  }
});
