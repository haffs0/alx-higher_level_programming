#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
