import { useState } from "react";
import friendsList from "./friends.json"

import FormSplitBill from "./components/FormSplitBill";
import FriendListCard from "./components/FriendListCard";
import FormAddFriend from "./components/FormAddFriend";

function App() {
  const [friends, setFriends] = useState(friendsList);
  const [showAddFriend, setShowAddFriend] = useState(false);

  const handleShowAddFriend = () => {
    setShowAddFriend(showAddFriend => !showAddFriend);
  }

  const onAddNewFriend = friend => {
    setFriends(friends => [...friends, friend]);
  }

  return (
    <>
     <div className="app">
      <div className="sidebar">
        <FriendListCard
          friends={friends}
        />
        {showAddFriend && <FormAddFriend onAddNewFriend={onAddNewFriend}/>}
        <button className="button" onClick={handleShowAddFriend}>
          {showAddFriend ? "Tutup" : "Tambah Teman"}
        </button>
      </div>
      <FormSplitBill />
    </div>
    </>
  )
}

export default App
