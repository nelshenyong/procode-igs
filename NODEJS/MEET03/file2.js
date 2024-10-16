const fs = require('fs');

    //writing files
    fs.writeFile('Blox.txt', 'hello, world', () => {
    console.log('file was written');
});

fs.writeFile('blox2.txt', 'hello, again', () => {
    console.log('files was written');
});

    // reading files
fs.readFile('blox.txt', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data.toString());
});

    // creating directory
fs.mkdir('./assets', err => {
    if (err) {
        console.log(err);
    }
    console.log('folder created');
});

//deleting directory
fs.rmdir('./assets', err => {
    if (err) {
        console.log(err);
    }
    console.log('folder deleted');
});

// deleting files
if (fs.existsSync('deleteme.txt')) {
    fs.unlink('deleteme.txt', err => {
        if (err) {
            console.log(err);
        }
        console.log('file deleted');
    });
}

