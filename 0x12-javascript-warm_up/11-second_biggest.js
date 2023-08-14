#!/usr/bin/node
const n = process.argv.length;
if (n < 4) console.log('0');
else {
  const myNums = [];
  for (let i = 2; i < n; i++) myNums.push(+process.argv[i]);
  // sorting descendingly by value not lexicographicly
  myNums.sort((a, b) => b - a);
  console.log(myNums[1]);
}
