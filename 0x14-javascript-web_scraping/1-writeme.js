#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  process.exit(1);
}

try {
  fs.writeFileSync(filePath, contentToWrite, 'utf-8');
} catch (error) {
  console.error(`An error occurred while writing to the file: ${error}`);
}
