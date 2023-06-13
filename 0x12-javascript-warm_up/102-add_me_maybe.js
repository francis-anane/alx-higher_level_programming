#!/usr/bin/node

/* Increments and call a function */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
