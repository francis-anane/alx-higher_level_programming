#!/usr/bin/node

/* computes the number of tasks completed by user based on 'id' */

const request = require('request'); // import request module

if (process.argv.length === 3) {
  const url = process.argv[2]; // Todos API url 'https://jsonplaceholder.typicode.com/todos'
  // Make an http Get request
  request.get(url, (err, response, body) => {
    if (!err) {
      const todos = JSON.parse(body);
      const completed = []; // To store completed todo by users
      const userIds = {}; // Store User ids and the number of completed tasks
      for (let i = 0; i < todos.length; i++) {
        if (todos[i].completed === true) {
          completed.push(todos[i]); // update list of completed tasks
        }
      }
      for (let i = 0; i < completed.length; i++) {
        const uid = completed[i].userId.toString();
        if (uid in userIds) {
          userIds[uid]++; // Increment tasks completed by user id
        } else {
          userIds[uid] = 1; // Add new id and completed task
        }
      }
      console.log(userIds);
    }
  });
}
