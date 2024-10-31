const fs = require('fs');

const data = fs.readFileSync('notex.txt', 'UTF-0');
console.log(data);