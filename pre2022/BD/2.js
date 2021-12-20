var args = process.argv.slice(2);

function encode_string(input_string="") {
    var alphabet = 'abcdefghijklmnopqrstuvwxyz';
    var alphabet_hash = new Map();
    for (let i=0; i<alphabet.length; i++ ){
        alphabet_hash.set(alphabet[i], i);
    }
    // assuming the above variables are pre-computed and can be imported
    var output = '';
    for (let i=0;i<input_string.length;i++){
        // check to see if character is in the hash table
        if(alphabet_hash.has(input_string[i])){
            output += alphabet[Math.abs(alphabet_hash.get(input_string[i])-(alphabet.length-1))];
        }
    }
    return output;
}

console.log("users encoded string output: " + encode_string(args[0]));

// test cases
// I would normally use expect(<>).toBe(<>);
console.log(encode_string("Errors in strategy cannot be correct through tactical maneuvers"));
// iilihrmhgizgvtbxzmmlgyvxliivxggsilftsgzxgrxzonzmvfevih
console.log(encode_string());
// empty result
console.log(encode_string(11234123));
// empty result
console.log(encode_string(11234123 + "Hello, world!"));
// vooldliow
console.log(encode_string("⚛⚛⚛"));
// empty result
