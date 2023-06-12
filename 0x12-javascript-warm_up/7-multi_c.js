#!/usr/bin/node

/* print x times of "C is fun" where "x" a type that can be converted into a
 Number data type from a passed argument to the  script
*/

if (process.argv[2] === undefined || isNaN(process.argv[2]))
{
    console.log('Missing number of occurrences');
}
else
{
    const x = Number(process.argv[2]);
    let counter = 0;
    while (counter < x)
    {
	console.log('C is fun');
	counter++;
    }
}
