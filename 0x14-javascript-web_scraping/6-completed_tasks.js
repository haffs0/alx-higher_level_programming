#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    let results = {};
    let json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      let task = json[i];
      if (task.completed) {
        if (results[task.userId] === undefined) {
          results[task.userId] = 1;
        } else {
          results[task.userId] += 1;
        }
      }
    }
    console.log(results);
  }
});
