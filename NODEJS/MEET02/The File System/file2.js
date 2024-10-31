const fs = require('fs');

// Writing files
fs.writeFile('blog.txt', 'hello, world', () => {
    console.log('files was written');
});

fs.writeFile('blog2.txt', 'hello, again', () => {
    console.log('files was written');
});

// Reading files
fs.readFile('blog.txt', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data.toString);
});

fs.readFile('blog2.txt', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data.toString);
});

    
// Creting directory
fs.mkdir('./assets', err => {
    if (err) {
        console.log(err);
    }
    console.log('folder created')
})