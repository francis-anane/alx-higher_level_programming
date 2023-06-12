#!/usr/bin/node

/* Converts first argument to the script into a number and print it,
else print "Not a number" in argument can't be converted
*/

if (process.argv[2] === undefined || isNaN(process.argv[2]))
{
    console.log('Not a number');
}
else
{
    console.log('My number:', parseInt(process.argv[2]));
}
