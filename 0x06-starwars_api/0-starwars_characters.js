#!/usr/bin/env node

const request = require('request-promise-native');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;
const names = [];

const requestCharacters = async () => {
  try {
    const response = await request(filmEndPoint);
    const jsonBody = JSON.parse(response);
    return jsonBody.characters;
  } catch (error) {
    console.error('Error:', error);
    return [];
  }
};

const requestNames = async (characters) => {
  try {
    const promises = characters.map(async (character) => {
      const response = await request(character);
      const jsonBody = JSON.parse(response);
      return jsonBody.name;
    });
    return Promise.all(promises);
  } catch (error) {
    console.error('Error:', error);
    return [];
  }
};

const getCharNames = async () => {
  try {
    const characters = await requestCharacters();
    if (characters.length > 0) {
      const charNames = await requestNames(characters);
      process.stdout.write(charNames.join('\n') + '\n');
    } else {
      console.error('Error: Got no Characters for some reason');
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

getCharNames();

