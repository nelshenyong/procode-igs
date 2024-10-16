import { createBrowserRouter } from 'react-router-dom';
import Layout from '../pages/Layout';
import Index from "../pages/Index";
import About from '../pages/About';
import Blog from '../pages/Blog';

// export const router = createBrowserRouter([
//     {
//         path : '/',
//         element : <Index />,
//     },
//     {
//         path : '/about',
//         element : <About />,
//     },
//     {
//         path : '/blog',
//         element : <Blog />,
//     },
// ])

export const router = createBrowserRouter([
    {
        path : '/',
        element : <Layout />,
        children : [
            {
                path : '/',
                element : <Index />,
            },
            {
                path : '/about',
                element : <About />,
            },
            {
                path : '/blog',
                element : <Blog />,
            },
        ]
    }
])