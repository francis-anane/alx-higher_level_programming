#!/usr/bin/node
/*Reads and prints the content of a file passed as CLI argument.*/

const fs = require("fs"); // import file system

if (process.argv.length == 3){
    //The readFile method takes filename, encoding, and callback function as parameter
    let content = fs.readFile(process.argv[2], "utf-8", (err, data) => {
	if (err){
	    console.log(err);
	} else {
	    console.log(data);
	}
    });
}
