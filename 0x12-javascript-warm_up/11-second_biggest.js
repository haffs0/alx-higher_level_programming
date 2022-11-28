#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (args.length === 3 || !args[2]) {
  console.log(0);
} else {
  const sortArray = args.slice(2).sort();
  console.log(sortArray[sortArray.length - 2]);
}
