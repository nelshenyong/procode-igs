const fs = require('fs');

const data = fs.readFIleSync('notes.txt', 'UTF-8');
console.log(data);