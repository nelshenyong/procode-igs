const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const Blog = require('./models/blog');

const app = express();
const urlencodedParser = bodyParser.urlencoded({ extended: false });

const dbURI = 'mongodb+srv://admin:Admin1234@cluster0.cfzga.mongodb.net/nodejs-app?retryWrites=true&w=majority&appName=Cluster0';
mongoose.connect(dbURI)
        .then(result => {
          console.log('connected to db');
          const PORT = 3000;
          app.listen(PORT, () => {
              console.log(`Server is running on http://127.0.0.1:${PORT}`);
          });
        })
        .catch(err => console.log(err));

app.set('view engine', 'ejs');
app.use(express.static('public'));

// app.get('/', (req, res) => {
//   const blogs = [
//     {title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur'},
//     {title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur'},
//     {title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur'},
//   ];
//   res.render('index', { title: 'Home', blogs });
// });

app.get('/', (req, res) => {
  res.redirect('/blogs');
})

app.get('/blogs', (req, res) => {
  Blog.find().sort({ createdAt : -1})
    .then( result => {
      res.render('index', {blogs: result, title: 'All blogs'});
    })
    .catch()
})

app.post('/blogs', urlencodedParser, (req, res) => {
    // console.log(req.body)
    const blog = new Blog(req.body);
  
    blog.save()
      .then(result => {
        res.redirect('/blogs');
      })
      .catch(err => {
        console.log(err);
      });
});

app.get('/about', (req, res) => {
  res.render('about', { title: 'About' });
});

app.get('/blogs/create', (req, res) => {
  res.render('create', { title: 'Create a new blog' });
});

app.get('/blogs/:id', (req, res) => {
  const id = req.params.id;
  Blog.findById(id)
    .then(result => {
      res.render('details', { blog: result, title: 'Blog Details' });
    })
    .catch(err => {
      console.log(err);
    });
});


// Sandbox Route
app.get('/add-blog', (req, res) => {
  const blog = new Blog({
      title: 'new blog 4',
      snippet: 'about my new blog',
      body: 'more about my new blog'
  })

  blog.save()
      .then(result => {
      res.send(result);
      })
      .catch(err => {
      console.log(err);
      });
});

app.get('/single-blog', (req, res) => {
  Blog.findById('66d138655e9329cd6add533a')
    .then(result => {
      res.send(result);
    })
    .catch(err => {
      console.log(err);
    });
});

app.get('/all-blogs', (req, res) => {
  Blog.find()
    .then(result => {
      res.send(result);
    })
    .catch(err => {
      console.log(err);
    });
});

app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
});