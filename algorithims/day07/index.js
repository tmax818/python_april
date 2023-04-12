/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
// {a: true}
const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

const str5 = "hellooe";
const expected5 = "helo";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
  if(str === ""){
    return str
  }
  let new_str = ""
  const seen = {} // {h: true, e: true }
   for(let i = 0; i < str.length; i++){
    console.log(seen)
      if(!seen[str[i]]){
        new_str += str[i]
        seen[str[i]] = true;
      }
   }
   return new_str
}

// console.log(stringDedupe(str1))
// console.log(stringDedupe(str2))
// console.log(stringDedupe(str3))
// console.log(stringDedupe(str4))
console.log(stringDedupe(str5))