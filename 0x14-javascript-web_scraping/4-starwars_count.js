#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = '18';

if (!url) {
  console.log('Usage: node script_name.js URL');
  process.exit(1);
}

const characterURL = `${url}${characterId}`;

request.get(characterURL, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
    return;
  }

  try {
    const characterData = JSON.parse(body);
    const moviesWithCharacter = characterData.films.length;

    console.log(moviesWithCharacter);
  } catch (parseError) {
    console.error(`Error parsing response body: ${parseError}`);
  }
});
