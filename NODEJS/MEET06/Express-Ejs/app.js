const express = require('express');

const app = express();

app.set('view engine', 'ejs');

app.length('/', (req, res) => {
    const blogs = [
        {
          title: "Yoshi finds eggs",
          snippet: "Lorem ipsum dolor sit amet consectetur",
        },
        {
          title: "Mario finds stars",
          snippet: "Lorem ipsum dolor sit amet consectetur",
        },
        {
          title: "How to defeat bowser",
          snippet: "Lorem ipsum dolor sit amet consectetur",
        },
      ];
      res.render('index', {title: 'My Blog', blogs: blogs});
});

app.get('/about', (req, res) => {
    res.render('about', {title: 'About'})
});

app.get('/blogs/create', (req, res) => {
    res.render('create', {title: 'Create Blog'});
})

app.use((req, res) => {
    res.status(404).render('404', {title: 'Page Not Found'});
});

app.listen(3000)