#!/usr/bin/node
const movieID = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + movieID, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
