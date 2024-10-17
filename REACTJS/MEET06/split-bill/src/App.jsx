import { useState } from "react";
import friendsList from "./friends.json"

import FormSplitBill from "./components/FormSplitBill";
import FriendListCard from "./components/FriendListCard";

function App() {
  const [friends, setFriends] = useState(friendsList);

  return (
    <>
     <div className="app">
      <div className="sidebar">
        <FriendListCard
          friends={friends}
        />
      </div>
      <FormSplitBill />
    </div>
    </>
  )
}

export default App
