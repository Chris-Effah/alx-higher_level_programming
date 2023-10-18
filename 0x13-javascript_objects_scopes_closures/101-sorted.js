#!/usr/bin/node
const dict = require('./101-data').dict;

function computeUserIdsByOccurrences (dict) {
  const userIdsByOccurrences = {};

  for (const userId in dict) {
    const occurrences = dict[userId];

    if (!userIdsByOccurrences[occurrences]) {
      userIdsByOccurrences[occurrences] = [];
    }

    userIdsByOccurrences[occurrences].push(userId);
  }

  return userIdsByOccurrences;
}

const result = computeUserIdsByOccurrences(dict);

console.log(result);
