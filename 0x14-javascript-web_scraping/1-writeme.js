#!/usr/bin/node

const filePath = process.argv[2];
const dataToWrite = process.argv[3];

const fs = require('fs');

fs.writeFile(filePath, dataToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
