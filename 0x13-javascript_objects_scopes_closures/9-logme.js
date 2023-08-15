#!/usr/bin/node
let nbPrinted = 0;
exports.logMe = function (item) {
  console.log(`${nbPrinted}: ${item}`);
  nbPrinted++;
};
