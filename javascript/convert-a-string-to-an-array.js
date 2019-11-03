// https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/javascript

const chai = require("chai");

function stringToArray(string){

	return string.split(" ");

}

chai.assert.deepEqual(stringToArray("Robin Singh"), ["Robin", "Singh"]);
chai.assert.deepEqual(stringToArray("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"]);