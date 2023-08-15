#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((element, index) => element * list);
console.log(list);
console.log(newList);
