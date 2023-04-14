/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
  var start = 0
  var end = str.length -1

  for(let i = 0; i < str.length; i++){
    console.log(str[i] !== " ")
    }
  
  for(let i = str.length -1; i > 0; i--){
    console.log(str[i] !== " ")

  }

  console.log(start, end)

  
}

console.log(trim(str1))

/*****************************************************************************/