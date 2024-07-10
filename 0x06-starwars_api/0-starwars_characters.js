#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.log("You must pass film_id");
    return;
}

const film_id = process.argv[2];

function fetch(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(new Error(`Request failed with status code ${response.statusCode}`));
            } else {
                resolve(JSON.parse(body));
            }
        });
    });
}

fetch(`https://swapi-api.alx-tools.com/api/films/${film_id}`)
    .then(filmData => {
        const characterPromises = filmData.characters.map(characterUrl => fetch(characterUrl));
        return Promise.all(characterPromises);
    })
    .then(characters => {
        characters.forEach(character => {
            console.log(character.name);
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error.message);
    });
