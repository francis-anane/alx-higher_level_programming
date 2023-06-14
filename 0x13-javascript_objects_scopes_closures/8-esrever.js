#!/usr/bin/node
/* Return the reverse version of a list */

exports.esrever = function (list) {
  let index = 1; let tmp; let tmp2;
  const len = list.length;
  for (let half = (len / 2); half >= 1; half--) {
    tmp = list[index - 1]; /* get first element */
    tmp2 = list[len - index]; /* get last element */
    list[index - 1] = tmp2; /* put last element in first element's position */
    list[len - index] = tmp; /* put first element in last element's position */
    index++;
  }
  return list;
};
