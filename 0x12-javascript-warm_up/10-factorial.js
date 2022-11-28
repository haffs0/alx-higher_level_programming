#!/usr/bin/node

const process = require('process');

const args = process.argv;

function fact (num) {
  if (num === 1 || !num) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}

console.log(fact(Number(args[2])));
