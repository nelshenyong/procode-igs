import { useState, useEffect } from "react";
import Article from '../components/Article'
import Search from "../components/Search"

import postsData from "../posts.json"

function Blog()
{
    const [externalPosts, setExternalPost] = useState([]);
    const [posts, setPosts] = useState(postsData);
    const [postLen, setPostLen] = useState(0);

    useEffect(()=>{
        console.log('Always rendered!');
    })

    useEffect(()=>{
        console.log('Rendered!');
    }, []);

    const onSearchChange = value => {
        const filteredPosts = postsData.filter(item => item.title.includes(value));
        setPosts(filteredPosts);
        setPostLen(filteredPosts.length);
    }

    useEffect(()=>{
        fetch('https://jsonplaceholder.typicode.com/posts')
          .then(response => response.json())
          .then(json => setExternalPost(json));
      }, []);


    return (
        <>
            <Search onSearchChange={onSearchChange} postLen={postLen}/>
            {posts.map((props, index) => (
                <Article {...props} key={index} />
            ))}
            <h1>External Post</h1>
            {externalPosts.map((item, index) => (
                <div key={index}>
                    -{item.title}
                </div>
            ))}
        </>
    )
}

export default Blog;