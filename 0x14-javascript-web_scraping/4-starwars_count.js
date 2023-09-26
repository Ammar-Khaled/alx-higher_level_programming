#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const ourCharacter = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(response.body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j] === ourCharacter) {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
