import React from 'react';

const Navbar = ({ toggleDarkMode }) => {
    return (
        <nav>
            <h1>Simulasi KPR</h1>
            <button onClick={toggleDarkMode}>Toggle Dark Mode</button>
        </nav>
    );
};

export default Navbar;