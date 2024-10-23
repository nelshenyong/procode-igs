import { useState, useEffect } from "react";
import friendsList from "./friends.json";
import FormSplitBill from "./components/FormSplitBill";
import FriendListCard from "./components/FriendListCard";
import FormAddFriend from "./components/FormAddFriend";

function App() {
    const [friends, setFriends] = useState(() => {
        const savedFriends = localStorage.getItem('friends');
        return savedFriends ? JSON.parse(savedFriends) : friendsList;
    });
    const [showAddFriend, setShowFriend] = useState(false);
    const [selectedFriend, setSelectedFriend] = useState(null);

    useEffect(() => {
        // menerima data friends dari localStorage
        localStorage.setItem('friends', JSON.stringify(friends));
    }, [friends]);

    const handleShowAddFriend = () => setShowFriend((prev) => !prev);

    const onAddNewFriend = (friend) => {
        setFriends((prevFriends) => [...prevFriends, friend]);
    };

    function onSelectedFriend(friend) {
        setSelectedFriend((selected) =>
            selected?.id === friend.id ? null : friend
        );
        setShowFriend(false);
    }

    function handleSplitBill(value) {
        setFriends((prevFriends) =>
            prevFriends.map((friend) =>
                friend.id === selectedFriend?.id
                    ? { ...friend, balance: friend.balance + value }
                    : friend
            )
        );
        setSelectedFriend(null);
    }
    
    // Fungsi untuk menghapus teman
    function handleDeleteFriend(id) {
        setFriends((prevFriends) => prevFriends.filter(friend => friend.id !== id));
        // periksa apakah teman yang dihapus sedang dipilih
        // jika iya, hapus
        if (selectedFriend && selectedFriend.id === id) {
            setSelectedFriend(null);
        }
    }

    return (
        <div className="app">
            <div className="sidebar">
                <FriendListCard
                    friends={friends}
                    onSelectedFriend={onSelectedFriend}
                    selectedFriend={selectedFriend}
                    onDeleteFriend={handleDeleteFriend}
                />
                {showAddFriend && <FormAddFriend onAddNewFriend={onAddNewFriend} />}
                <button className="button" onClick={handleShowAddFriend}>
                    {showAddFriend ? "Tutup" : "Tambah Teman"}
                </button>
            </div>
            {selectedFriend && (
                <FormSplitBill
                    selectedFriend={selectedFriend}
                    handleSplitBill={handleSplitBill}
                />
            )}
        </div>
    );
}

export default App;