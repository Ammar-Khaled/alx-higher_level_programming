#!/usr/bin/node
const n = process.argv.length;
if (n < 4) console.log('0');
else {
  const  myNums = [];
  for (let i = 2; i < n; i++) myNums.push(+process.argv[i]);
  myNums.sort();
  console.log(myNums[n - 4]);
}
