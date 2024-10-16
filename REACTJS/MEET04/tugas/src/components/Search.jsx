import { useState } from "react";

export default function Search({onSearchChange, postLen})
{
    const [search, setSearch] = useState("");
    const [isSearchTriggered, setIsSearchTriggered] = useState(false);

    const onSearchHandler = event => {
        // console.log("Search Component : "+event.target.value);
        setSearch(event.target.value);
        setIsSearchTriggered(false);
        // onSearchChange(event.target.value);
    }

    const onClickSearchBtnHandler = () => {
        setIsSearchTriggered(true);
        onSearchChange(search);
    };

    const onKeyDownSearchHandler = event => {
        if (event.key === 'Enter') {
            onClickSearchBtnHandler();
        }
        };
    
    return (
        <>
        <div>
            Cari Artikel : 
            <input 
                onChange={onSearchHandler} 
                onKeyDown={onKeyDownSearchHandler}
            ></input>
            <button onClick={onClickSearchBtnHandler}>cari</button>
        </div>
        {isSearchTriggered && (
            <small>ditemukan {postLen} data dengan pencarian kata "{search}"</small>
        )}
        </>
    )
}