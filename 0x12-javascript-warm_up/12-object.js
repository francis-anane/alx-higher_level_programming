#!/usr/bin/node
/* Replace the value 12 with 89 in the object*/
const myObject = {
    type: 'object',
    value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
