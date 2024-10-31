import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Quote from './components/Quote';
import InputForm from './components/InputForm';
import Result from './components/Result';
import Footer from './components/Footer';

const App = () => {
    const [results, setResults] = useState({});
    const [darkMode, setDarkMode] = useState(false);

    const handleCalculate = (results) => {
        setResults(results);
    };

    const toggleDarkMode = () => {
        setDarkMode (!darkMode);
    };

    return (
        <div className={darkMode ? 'dark-mode' : ''}>
            <Navbar toggleDarkMode={toggleDarkMode} />
            <Quote />
            <InputForm onCalculate={handleCalculate} />
            {Object.keys(results).length > 0 && <Result results={results} />}
            <Footer />
        </div>
    );
};

export default App;