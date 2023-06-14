#!/usr/bin/node
/* Convert a number from base 10 to another base passed as argument */
exports.converter = function (base) {
  return (num) => {
    return num.toString(base); /* convert to the base with toString method */
  };
};
