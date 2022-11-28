#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (!Number(args[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2], 10);
  let count = 1;

  while (count <= size) {
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
    count++;
  }
}
