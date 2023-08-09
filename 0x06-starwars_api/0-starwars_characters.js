#!/usr/bin/env node

const request = require('request');

function getCharacters(movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
  
  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const characterUrls = filmData.characters;
        const characterNames = [];
        
        Promise.all(characterUrls.map(url => fetchCharacterName(url)))
          .then(names => resolve(names))
          .catch(error => reject(error));
      }
    });
  });
}

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.length !== 1) {
    console.error('Usage: node script_name.js movie_id');
    process.exit(1);
  }
  
  const movieId = args[0];
  
  getCharacters(movieId)
    .then(characterNames => {
      if (characterNames.length === 0) {
        console.log('No characters found for the provided movie ID.');
      } else {
        characterNames.forEach(name => console.log(name));
      }
    })
    .catch(error => {
      console.error('An error occurred:', error);
    });
}

main();



