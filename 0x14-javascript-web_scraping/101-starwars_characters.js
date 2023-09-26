#!/usr/bin/node
let id = parseInt(process.argv[2], 10);
const url = 'https://swapi-api.alx-tools.com/api/films/';
let characters = [];
const request = require('request');
request(url, (error, response, body) => {
  if (error == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }


    for (let k = 0; k < results.length; k++) {
      if (results[k].episode_id === id) {
        characters = results[k].characters;
        break;
      }
    }

    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, resp, body) => {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
