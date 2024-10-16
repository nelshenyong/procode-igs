import React from 'react';
import Navbar from './components/Navbar.jsx';
import Hero from './components/Hero.jsx';
import Features from './components/Features.jsx';
import FAQSection from './components/FAQSection.jsx';
import Footer from './components/Footer.jsx';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <Navbar />
      </header>
      <main>
        <Hero />
        <Features />
        <FAQSection />
      </main>
      <Footer />
    </div>
  );
}

export default App;