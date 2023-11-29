#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Movie ID from command line argument

if (!movieId) {
  console.log('Usage: node script_name.js movie_id');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`An error occurred while making the request: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } catch (parseError) {
    console.error(`Error parsing response body: ${parseError}`);
  }
});
