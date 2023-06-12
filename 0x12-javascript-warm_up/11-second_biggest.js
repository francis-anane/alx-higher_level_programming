#!/usr/bin/node
/* searches the second biggest integer in the list of arguments passed
to the script.*/
if (process.argv.length <= 3)
{
    console.log('0');
}
else
{
    const args = process.argv.slice(2).map(Number);

    /*sort in descending order with a compare function*/
    const sort_args = args.sort(function (a, b) { return b - a; });
    /*print second biggest*/
    console.log(sort_args[1]);
}
