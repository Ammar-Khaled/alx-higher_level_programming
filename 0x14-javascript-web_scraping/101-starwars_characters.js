#!/usr/bin/node
const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
function getCharacterName (characterUrl) {
  return new Promise(
    (resolve, reject) => {
      request(characterUrl, (err, res) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(res.body).name);
        }
      });
    }
  );
}
const request = require('request');
request(url + filmId, (error, response) => {
  if (error == null) {
    const characterUrls = JSON.parse(response.body).characters;
    Promise.all(characterUrls.map(getCharacterName)).then(function (names) {
      for (let i = 0; i < names.length; i++) {
        console.log(names[i]);
      }
    });
  }
});
