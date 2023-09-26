#!/usr/bin/node

const file_path = process.argv[2];

const fs = require('fs');

fs.readFile(file_path, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    }
    else {
        console.log(data);
    }
});
