/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const y = String(x);
    const reversedString = y.split("").reverse().join(""); 
    return y==reversedString;


};