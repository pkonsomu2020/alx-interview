#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`API request failed with status code ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);

  if (!movieData.characters || movieData.characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  const characterUrls = movieData.characters;

  // Function to fetch and print character names
  const printCharacterNames = (characterUrls, index = 0) => {
    if (index >= characterUrls.length) {
      return;
    }

    request(characterUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Character request failed with status code ${charResponse.statusCode}`);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Continue to the next character
      printCharacterNames(characterUrls, index + 1);
    });
  };

  // Start fetching and printing character names
  printCharacterNames(characterUrls);
});
