#!/usr/bin/node

const request = require('request');

// Get movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL for the Star Wars API with the specified movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Helper function to fetch each character's name in sequence
  function fetchCharacter(index) {
    if (index >= characters.length) {
      return; // All characters have been fetched
    }

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Fetch the next character in sequence
      fetchCharacter(index + 1);
    });
  }

  // Start fetching characters from the first one
  fetchCharacter(0);
});
