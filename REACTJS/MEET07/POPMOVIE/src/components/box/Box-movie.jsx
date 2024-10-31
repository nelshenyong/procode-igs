import { useState, useEffect } from "react";
function BoxMovies({ children }) {
    const [isOpen, setIsOpen] = useState(true);
    return (
      <div className="box">
        <button className="btn-toggle" onClick={() => setIsOpen((open) => !open)}>
          {isOpen ? "😍" : "+"}
        </button>
        {isOpen && children}
      </div>
    );
}
export  default BoxMovies;
