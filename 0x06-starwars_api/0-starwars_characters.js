#!/usr/bin/node

const request = require('request');

const getInfo = (apis, i = 0) => {
  if (i === apis.length) return;
  request(apis[i], function (err, res, body) {
    if (err) {
      throw err;
    }
    const dta = JSON.parse(body).name;
    console.log(dta);
    getInfo(apis, i + 1);
  });
};

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    throw error;
  }
  const dta = JSON.parse(body).characters;
  getInfo(dta);
  // console.log(dta);
});
