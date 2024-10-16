import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import Handlebars from 'handlebars';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function renderTemplate(templatePath, data, callback) {
    fs.readFile(templatePath, 'utf-8', (err, souce) =>{
        if (err){
            return callback;
        }
        const template = Handlebars.compile(souce);
        const result = template(data);
        callback(null, result);
    });
}

const server = http.createServer((req, res) =>{
    res.setHeader('Content-Type', 'text/html');
    if (req.url ==='/'){
        const templatePath = path.join(__dirname, 'templates', 'home.html');
        const data = {
            tittle: "simplt html handlebards example",
            welcomeMessage: 'Welcome to our simple server'
        }

        renderTemplate(templatePath, data, (err, html) =>{
            if (err){
                res.writeHead(500, {'Content-Type': "text/plain"});
                res.end('Server Error');
            }else{
                res.statusCode = 200;
                res.end(html);
            }
        })
    }else if (req.url === '/juan'){
        res.statusCode = 200;
        res.end('<h1>hello, juan</h1>');
    } else if (req.url ==='/about'){
        // isi
    } 
    else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('404 not Found !');
    }
});

const port = 3000;
const host = '127.0.0.1' //0.0.0.0
server.listen(port, ()=>{
    console.log(`Server is running on http://${host}:${port}`);
});