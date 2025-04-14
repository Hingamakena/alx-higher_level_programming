#!/usr/bin/node

const {argv} = require('node:process');

for (let i =1; argv[i] != null; i++){
	if (argv[i] <= 1){
		console.log("No Argument");
	}
	else if (argv[i] > 1 && argv[i] < 3){
		console.log("Argument found");
	}
	else
		console.log("Arguments found");
}
