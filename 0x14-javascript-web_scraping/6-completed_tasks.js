#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Filter completed tasks
    const completedTasks = tasks.filter(task => task.completed);

    // Create an object to store the count for each user ID
    const completedTasksCount = {};

    // Count completed tasks for each user ID
    completedTasks.forEach(task => {
      const userId = task.userId.toString();
      if (completedTasksCount[userId] === undefined) {
        completedTasksCount[userId] = 1;
      } else {
        completedTasksCount[userId]++;
      }
    });
    console.log(completedTasksCount);
  }
});
