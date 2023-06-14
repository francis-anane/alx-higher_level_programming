#!/usr/bin/node
/* returns the number of times an element in a list */
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const element of list) {
    if (searchElement === element) {
      occurrences++;
    }
  }
  return occurrences;
};
