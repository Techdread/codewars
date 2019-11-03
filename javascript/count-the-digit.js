// https://www.codewars.com/kata/count-the-digit/train/javascript

const chai = require("chai");

function countOcurrences(str, value) {
    var regExp = new RegExp(value, "gi");
    return (str.match(regExp) || []).length;
  }

function nbDig(n, d) {
    let count = 0;
    let digit = d.toString();
    for(i = 1; i <= n; i++){
        count+=countOcurrences((i * i).toString(), digit);
        //count+= (i * i).toString().split(digit).length - 1;
    }
    return count;
}

chai.assertEquals(nbDig(5750, 0), 4700)
chai.assertEquals(nbDig(11011, 2), 9481)
chai.assertEquals(nbDig(12224, 8), 7733)
chai.assertEquals(nbDig(11549, 1), 11905)
