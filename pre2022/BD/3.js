var args = process.argv.slice(2);
function g(input_string=""){
    var alphabet = "abcdefghijklmnopqrstuvwxyz";
    var alphabet_hash = {};
    for (var i=0; i<alphabet.length; i++ ){
        alphabet_hash[alphabet[i]] = 0;
    }
    var output = '';
    for (i=0;i<input_string.length;i++){
        if(typeof(alphabet_hash[input_string[i].toLowerCase()]) === "number")
        alphabet_hash[input_string[i].toLowerCase()]++;
    }
    return alphabet_hash;
}

console.log(`users string "${args[0]}" frequency table:`);

// test cases
// I would normally use expect(<>).toBe(<>);
console.log(g("Hello there! Apple!"));
// {
//         a:1,
//         b:0,
//         c:0,
//         d:0,
//         e:4,
//         f:0,
//         g:0,
//         h:2,
//         i:0,
//        j:0,
//        k:0,
//        l:3,
//        m:0,
//       n:0,
//      o:1,
//      p:2,
//      q:0,
//      r:1,
//      s:0,
//      t:1,
//      u:0,
//      v:0,
//      w:0,
//      x:0,
//      y:0,
//      z:0
// }

console.log(g("Errors in strategy cannot be correct through tactical maneuvers"));
//{ a: 5,
// b: 1,
// c: 5,
// d: 0,
// e: 6,
// f: 0,
// g: 2,
// h: 2,
// i: 2,
// j: 0,
// k: 0,
// l: 1,
// m: 1,
// n: 4,
// o: 4,
// p: 0,
// q: 0,
// r: 8,
// s: 3,
// t: 7,
// u: 2,
// v: 1,
// w: 0,
// x: 0,
// y: 1,
// z: 0 }
console.log(g());
// all 0
console.log(g(11234123));
// all 0
console.log(g(11234123 + "Hello, world!"));
// { a: 0,
// b: 0,
// c: 0,
// d: 1,
// e: 1,
// f: 0,
// g: 0,
// h: 1,
// i: 0,
// j: 0,
// k: 0,
// l: 3,
// m: 0,
// n: 0,
// o: 2,
// p: 0,
// q: 0,
// r: 1,
// s: 0,
// t: 0,
// u: 0,
// v: 0,
// w: 1,
// x: 0,
// y: 0,
// z: 0 }
console.log(g("⚛⚛⚛"));
// all 0

