#!/usr/bin/node
/* prints the number of arguments already printed and the new argument value */

let printCount = 0;

exports.logMe = function (item) {
  console.log(printCount + ': ' + item);
  printCount++;
};
