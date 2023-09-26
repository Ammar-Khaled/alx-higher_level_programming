#!/usr/bin/node
const movieId = parseInt(process.argv[2], 10);
const url = 'https://swapi-api.alx-tools.com/api/films/';
let characters = [];
const request = require('request');
request(url, (error, response) => {
  if (error == null) {
    let episodeId = 0;
    if (movieId < 4) {
      episodeId = movieId + 3;
    } else {
      episodeId = movieId - 3;
    }
    const results = JSON.parse(response.body).results;

    for (let k = 0; k < results.length; k++) {
      if (results[k].episode_id === episodeId) {
        characters = results[k].characters;
        break;
      }
    }

    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, resp) => {
        if (err == null) {
          console.log(JSON.parse(resp.body).name);
        }
      });
    }
  }
});
