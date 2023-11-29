#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line argument

if (!filePath) {
  console.log('Usage: node script_name.js file_path');
  process.exit(1);
}

try {
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  console.log(fileContent);
} catch (error) {
  console.error(`An error occurred while reading the file: ${error}`);
}
