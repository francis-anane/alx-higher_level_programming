#!/usr/bin/node

/* computes the number of tasks completed by user based on 'id' */

const request = require('request'); // import request module

if (process.argv.length === 3) {
  const url = process.argv[2]; // Todos API url 'https://jsonplaceholder.typicode.com/todos'
  // Make an http Get request
  request.get(url, (err, response, body) => {
    if (!err) {
      const todos = JSON.parse(body);
      const completed = {}; // To store user id and number of completed todos by user id
      for (let i = 0; i < todos.length; i++) {
        if (todos[i].completed === true) {
          // console.log(todos[i]);
          const uid = todos[i].userId;
          if (uid in completed) {
            completed[uid]++; // update of completed tasks
          } else {
            completed[uid] = 1;
          }
        }
      }
      console.log(completed);
    }
  });
}
