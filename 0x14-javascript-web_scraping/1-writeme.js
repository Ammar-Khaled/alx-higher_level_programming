#!/usr/bin/node

const filePath = process.argv[2];
const dataToWrite = process.argv[3];

const fs = require('fs');

fs.writeFile(filePath, 'utf8', dataToWrite, (err) => {
  if (err) {
    console.error(err);
  }
});
