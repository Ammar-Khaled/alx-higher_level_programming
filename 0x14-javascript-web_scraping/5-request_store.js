#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, response) => {
  if (error == null) {
    fs.writeFile(filePath, response.body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
