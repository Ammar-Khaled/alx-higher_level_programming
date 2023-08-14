#!/usr/bin/node
function fact (n) {
  if (n === 1 || n === 0) return (1);

  return (n * fact(n - 1));
}

const n = +process.argv[2];
if (isNaN(n)) console.log('1');
else console.log(fact(n));
