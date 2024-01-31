#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    theCharacters(characters, 0);
  }
});

function theCharacters (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        theCharacters(characters, idx + 1);
      }
    }
  });
}
