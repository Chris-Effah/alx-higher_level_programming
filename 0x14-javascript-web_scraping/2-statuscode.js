#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // URL to request from command line argument

if (!url) {
  console.log('Usage: node script_name.js URL');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
