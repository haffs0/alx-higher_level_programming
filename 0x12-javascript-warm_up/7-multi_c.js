#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (!Number(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const times = parseInt(args[2], 10);
  let count = 1;

  while (count <= times) {
    console.log('C is fun');
    count++;
  }
}
