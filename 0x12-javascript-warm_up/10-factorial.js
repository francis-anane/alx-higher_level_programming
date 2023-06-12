#!/usr/bin/node
/* computes the factorial of a number with recursion, whereby number is first
argument to script  casted into an integer
*/
function factorial (num)
{
    if (num < 0)
    {
	return (-1);
    }
    if (num === 0 || isNaN(num))
    {
	return (1);
    }
    return (num * factorial(num - 1));
}

console.log(factorial(Number(process.argv[2])));
