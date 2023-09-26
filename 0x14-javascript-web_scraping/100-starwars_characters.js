#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
request(url + movieId, (error, response) => {
  if (error == null) {
    const characters = JSON.parse(response.body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, resp) => {
        if (err == null) {
          console.log(JSON.parse(resp.body).name);
        }
      });
    }
  }
});
