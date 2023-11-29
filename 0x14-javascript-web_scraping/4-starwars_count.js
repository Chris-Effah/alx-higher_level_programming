#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // API URL from command line argument
const characterId = '18'; // Character ID for Wedge Antilles

if (!apiUrl) {
  console.log('Usage: node script_name.js API_URL');
  process.exit(1);
}

const characterUrl = `${apiUrl}${characterId}`;

request.get(characterUrl, (error, response, body) => {
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

    console.log(`Number of movies where Wedge Antilles is present: ${moviesWithCharacter}`);
  } catch (parseError) {
    console.error(`Error parsing response body: ${parseError}`);
  }
});
