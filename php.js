// initialize the php parser factory class
const fs = require("fs");
const path = require("path");
const engine = require("php-parser");

// initialize a new parser instance
const parser = new engine({
  // some options :
  parser: {
    extractDoc: true,
    php7: true,
  },
  ast: {
    withPositions: true,
  },
});

// Retrieve the AST from the specified source
//const eval = parser.parseEval('echo "Hello World";');

// Retrieve an array of tokens (same as php function token_get_all)
const tokens = parser.tokenGetAll('<?php echo "Hello World";');

// Load a static file (Note: this file should exist on your computer)
//const phpFile = fs.readFileSync("./example.php");

// Log out results
console.log("Eval parse:", eval);
console.log("Tokens parse:", tokens);
// console.log("Filnodee parse:", parser.parseCode(phpFile));