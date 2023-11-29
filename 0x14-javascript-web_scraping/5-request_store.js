#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Usage: node script_name.js URL file_path');
  process.exit(1);
}

request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err}`);
      return;
    }
  });
});
